import pandas as pd
from bs4 import BeautifulSoup
import requests
import os
from colorthief import ColorThief
import matplotlib.pyplot as plt
from ColorConversion import ColorConversion
from ColorAnalysis import ColorAnalysis

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

Seasons = {
    "Winter": ["December", "January", "February"],
    "Spring": ["March", "April", "May"],
    "Summer": ["June", "July", "August"],
    "Fall": ["September", "October", "November"]
}




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

def get_season(month):
    """
    Get the season for a given month.

    Parameters:
    month (str): The month to get the season for.

    Returns:
    str: The season for the given month.
    """
    for season, months_in_season in Seasons.items():
        if month in months_in_season:
            return season
    return None



def main(csv_name="./data/architectural_digest_covers.csv"):
    """
    Main function to scrape Architectural Digest covers and featured articles and save them to a CSV file.

    Parameters:
    csv_name (str): The name of the CSV file to save the data to.
    """
    
    if not os.path.exists(csv_name) or os.path.getsize(csv_name) == 0:
        #populate the data frame with the scraped data and save to a csv file
        df = pd.DataFrame(get_all_issues(1922, 2025))
        df.to_csv(csv_name, index=False)
    else:
        print(f"{csv_name} already exists and is not empty. Skipping scraping and loading data from the existing file.")
    # Add a season column to the CSV file based on the month column if it doesn't already exist
    df = pd.read_csv(csv_name)
    if "season" not in df.columns:
        df["season"] = df["month"].apply(get_season)
        df.to_csv(csv_name, index=False)
    
    
   

    # Analyze the colors of the cover image from each row
    #if "primary_color" not in df.columns:
    for index, row in df.iterrows():
        cover_image_url = row["cover_image_url"]
        if cover_image_url:
            print(f"Getting cover data from: {row['year']} {row['month']}")
            color_analysis = ColorAnalysis(cover_image_url)
            palette = color_analysis.get_palette()
            df.at[index, "primary_color"] = ColorConversion.get_color_name(palette[0])
            for i, secondary_colors in enumerate(palette[1:], start=1):
                df.at[index, f"secondary_color_{i}"] = ColorConversion.get_color_name(secondary_colors)
    df.to_csv(csv_name, index=False)

    



if __name__ == '__main__':
    main()