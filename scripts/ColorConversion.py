import webcolors

class ColorConversion:
   

    @staticmethod
    def closest_color(requested_color):
        min_colors = {}
        
        # Iterate through all CSS3 colors supported by webcolors
        for name in webcolors.names("css3"):
        # Convert the name to its RGB equivalent
            rgb_value = webcolors.name_to_rgb(name)
            
            # Calculate Euclidean distance
            rd = (rgb_value.red - requested_color[0]) ** 2
            gd = (rgb_value.green - requested_color[1]) ** 2
            bd = (rgb_value.blue - requested_color[2]) ** 2
            
            min_colors[rd + gd + bd] = name
        
        # Find the name with the minimum distance
        return min_colors[min(min_colors.keys())]
    @staticmethod
    def get_color_name(requested_color):
        try:
            # Check if the exact color exists first
            closest_name = webcolors.rgb_to_name(requested_color)
        except ValueError:
            # If not, find the mathematically closest one
            closest_name = ColorConversion.closest_color(requested_color)
        
        return closest_name
        