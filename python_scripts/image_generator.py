from palette_code import RGB

class Image(object):

    def __init__(self, height, lenght):
        """
        This type will receive its dimensions so as to create the pixel matrix to generate the image.
        Initially, all pixels will have the RGB id (0, 0, 0), that is, black.
        """

        self.height = height
        self.lenght = lenght
        # This iteration will create the matrix.
        self.pixel_matrix = [[RGB(0, 0, 0) for _ in self.lenght] for _ in self.height]



    def inspect_pixel_coordinate(self, row, column):

        return self.pixel_matrix[row][column]

    def define_pixel_color(self, row, column, color:RGB):
        
        self.pixel_matrix[row][column] = color

    def open_ppm_file(self, filename):

        with open(filename, 'r') as ppm_archive:
            pass
        