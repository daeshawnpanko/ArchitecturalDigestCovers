import io

from colorthief import ColorThief
import requests
from PIL import Image
from sklearn.cluster import KMeans
from collections import Counter
import numpy as np

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

    # Deprecated method using ColorThief
    def get_palette(self, color_count=5):
        if not self.color_thief:
            self.fetch_image()
        self.palette = self.color_thief.get_palette(color_count=color_count)
        return self.palette
    
    def get_palette_NEW(self, num_colors=5):
        #Pull image from URL
        response = requests.get(self.image_url, timeout=10)
        response.raise_for_status() # Raises an error if the download failed (e.g., 404 or 500)

        raw_image = Image.open(io.BytesIO(response.content))
        image_rgb = raw_image.convert("RGB")
        
        image_array = np.array(image_rgb)
        
        #Reshape the image array (Flatten height and width into a single list of pixels)
        pixels = image_array.reshape(-1, 3)
        
        # Run the K-Means Machine Learning Model
        kmeans = KMeans(n_clusters=num_colors, random_state=42)
        labels = kmeans.fit_predict(pixels)
        
        # Extract the Color Coordinates
        palette = kmeans.cluster_centers_.astype(int)
        
        # Calculate Proportions
        counts = Counter(labels)
        total_pixels = len(labels)
        percentages = {i: counts[i]/total_pixels for i in range(num_colors)}
        
        return palette, percentages