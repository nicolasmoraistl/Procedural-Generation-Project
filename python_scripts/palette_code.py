class RGB:

    def __init__(self, r, g, b):

        """
        The data from this class correspond to the threefold scheme from the RGB system, 
        that will be represented by the variables r, g, b.
        """

        if 255 < r or r < 0 or 255 < g or g < 0 or 255 < b or b < 0:
            raise ValueError

        self.r = r
        self.g = g
        self.b = b

class Colorset:

    def __init__(self, filename = None):

        """
        It will kickstart the constructor by putting in place an empty colorset configuration
        """

        self.colorset = []
        if filename:
            with open(filename, 'r') as content:
                for hexa in content:
                    hexa.strip().lstrip('#')
                    if not hexa:
                        continue
                    hexa = hexa.strip().lstrip('#')
                    rgb = tuple(int(hexa[i:i+2], 16) for i in (0, 2, 4))
                    self.colorset.append(RGB(rgb[0], rgb[1], rgb[2]))
        

    def add_color_to_colorset(self, color:RGB):

        self.colorset.append(color)

    def check_amount_of_colors(self):

        return len(self.colorset)

    def check_color_by_index(self, index) -> RGB:

        return self.colorset[index]
