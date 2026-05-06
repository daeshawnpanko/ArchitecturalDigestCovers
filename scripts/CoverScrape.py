import pandas as pd
from bs4 import BeautifulSoup
import requests
"""This script scrapes the cover images and featured articles from Architectural Digest issues from 1922 through 2025."""

base_url = "https://archive.architecturaldigest.com/issues/"
issue_url = "https://archive.architecturaldigest.com/issue/"

months = [
    ("01", "January"),
    ("02", "February"),
    ("03", "March"),
    ("04", "April"),
    ("05", "May"),
    ("06", "June"),
    ("07", "July"),
    ("08", "August"),
    ("09", "September"),
    ("10", "October"),
    ("11", "November"),
    ("12", "December"),
]




def get_issue_data(issue):
    """
    Get the cover image URL and featured articles for a given issue of Architectural Digest.

    Parameters:
    issue (str): The URL of the issue to scrape.

    Returns:
    tuple: A tuple containing the cover image URL (or None if not found) and a list of featured articles (each article is a dictionary with 'title' and 'link' keys).
    
    """
    url = issue
    response = requests.get(url)
    if response.status_code != 200:
        return None, []
    soup = BeautifulSoup(response.content, "html.parser")
    
    # The magazine cover for this issue of AD
    cover_image = soup.find("img", class_="bndwgt__issuecover_main")
    cover_image_url = cover_image["src"] if cover_image else None
    
    # The 3 featured articles for this issue of AD, with links to the articles on the AD website (subscription probably required to red them though...)
    features = soup.find_all("div", class_="tpc_title")
    feature_list = []
    for feature in features:
        title = feature.find("a")["title"].strip().replace("View article: ", "")
        link = feature.find("a")["href"]
        feature_list.append({"title": title, "link": link})
    
    return cover_image_url, feature_list

def get_all_issues(start_year, end_year):
    """
    Scrape every article between the provided years

    Parameters:
    start_year (int): The starting year for scraping (inclusive).
    end_year (int):  The ending year for scraping (inclusive).
    
    Returns:
    all_issues(list): A list of dictionaries, each containing the year, month, cover image URL, and featured articles for an issue to be saved to a CSV file.
    """
    all_issues = []
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            url = f"{issue_url}{year}{month:02d}01"
            print(f"Getting data from: {url}")
            cover_image_url, features = get_issue_data(url)
            issue_data = {
                "year": year,
                "month": months[month - 1][1],
                "cover_image_url": cover_image_url,
                "features": features
            }
            if issue_data["cover_image_url"] or issue_data["features"]:
                all_issues.append(issue_data)
    return all_issues

def main(csv_name="./data/architectural_digest_covers.csv"):
    """
    Main function to scrape Architectural Digest covers and featured articles and save them to a CSV file.

    Parameters:
    csv_name (str): The name of the CSV file to save the data to.
    """
    df = pd.DataFrame(get_all_issues(1922, 2025))
    df.to_csv(csv_name, index=False)



if __name__ == '__main__':
    main()