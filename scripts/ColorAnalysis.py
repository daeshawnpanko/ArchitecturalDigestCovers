from colorthief import ColorThief
import requests

class ColorAnalysis:
    def __init__(self, image_url):
        self.image_url = image_url
        self.color_thief = None
        self.palette = None



    def fetch_image(self):
        response = requests.get(self.image_url)
        if response.status_code == 200:
            with open("temp_image.jpg", "wb") as f:
                f.write(response.content)
            self.color_thief = ColorThief("temp_image.jpg")
        else:
            raise Exception(f"Failed to fetch image from {self.image_url}")

    def get_palette(self, color_count=5):
        if not self.color_thief:
            self.fetch_image()
        self.palette = self.color_thief.get_palette(color_count=color_count)
        return self.palette