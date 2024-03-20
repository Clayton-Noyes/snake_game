import json

class Config:
    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            self.config_data = json.load(f)

    def get_color(self, color_name):
        return tuple(self.config_data['colors'][color_name])

    def get_display_size(self):
        return self.config_data['display_size']['width'], self.config_data['display_size']['height']

    def get_snake_properties(self):
        return self.config_data['snake_properties']['block_size'], self.config_data['snake_properties']['speed']

    def get_font_styles(self):
        return self.config_data['font_styles']['font_name'], self.config_data['font_styles']['score_font_size'], self.config_data['font_styles']['message_font_size']