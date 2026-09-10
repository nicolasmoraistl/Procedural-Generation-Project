class Palette(object):
    pass

class RGB(Palette):

    def __init__(self, r, g, b):

        """
        The data from this class correspond to the threefold scheme from the RGB system, 
        that will be represented by the variables r, g, b.
        """

        if 255 < r < 0 or 255 < g < 0 or 255 < b < 0:
            raise ValueError

        self.r = r
        self.g = g
        self.b = b

class Colorset(Palette):

    def create_empty_colorset(self):

        """
        It will kickstart the constructor by putting in place an empty colorset configuration
        """

        self.colorset = []

    def create_palette_by_archive(self, file):

        content = open(file, 'r')

        readable_content = content.read()

        for hex in readable_content:
            print(hex)
            self.colorset.append(hex)

        content.close()

    def add_color_to_colosert(self, color):

        self.colorset.append(color)

    def check_amount_of_colors(self):

        return len(self.colorset)

    def check_color_by_index(self, index):

        return self.colorset[index]
