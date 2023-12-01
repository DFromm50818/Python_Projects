import colorgram

c = colorgram
colors = c.extract("image.jpg",81)

class Extractor():
    def __init__(self):
        self.sized_color = len(colors)
        self.paint_colors = []

    def color_extractor(self):
        for rgb_color in colors:
            tuple_rgp = rgb_color.rgb
            r = tuple_rgp[0]
            g = tuple_rgp[1]
            b = tuple_rgp[2]
            self.paint_colors.append((r, g, b))

