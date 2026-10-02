from palette_code import RGB


class Image(object):

    def __init__(self, lenght, height):
        """
        This type will receive its dimensions so as to create the pixel matrix to generate the image.
        Initially, all pixels will have the RGB id (0, 0, 0), that is, black.
        """

        self.height = height
        self.lenght = lenght
        # This iteration will create the matrix.
        self.pixel_matrix = [[RGB(0, 0, 0) for _ in range(self.lenght)] for _ in range(self.height)]



    def inspect_pixel_coordinate(self, row, column):

        return self.pixel_matrix[row][column]

    def define_pixel_color(self, row, column, color:RGB):
        
        self.pixel_matrix[row][column] = color

    def open_ppm_file(self, ppm_file):



        with open(ppm_file, 'r') as read_archive:
            content = read_archive.read()
            tolken = content.split()
            l = int(tolken[1])
            h = int(tolken[2])
            pixels = [int(data) for data in tolken[4:]]
            
        idx = 0
        pixel_arq = []
        # Constructing image pixel matrix
        for y in range(h):
            row = []
            for x in range(l):
                color = RGB(pixels[idx], pixels[idx+1], pixels[idx+2])
                row.append(color)
                idx += 3
            pixel_arq.append(row)


        if h == self.height and l == self.lenght:
            self.pixel_matrix = pixel_arq
        else:
            ratio_height = h / self.height
            ratio_lenght = l / self.lenght

            for i in range(self.height):
                for j in range(self.lenght):
                    y = int(i * ratio_height)
                    x = int(j * ratio_lenght)
                    color = pixel_arq[y][x]
                    self.define_pixel_color(i, j, color)




            
            

    def save_ppm_image(self, path:str):

        """
        Reads the matrix + its header's parameters and generate a ppm image.

        Args:
        path: A string type that corresponds to the name of the path of the saved imagem.
        image: A list type that will represent the matrix.;

        Return:
        None
        """

        with open(path, 'w') as ppm_file:

            ppm_file.write("P3\n")
            ppm_file.write(f'{self.lenght} {self.height}\n')
            ppm_file.write('255\n')
            for y in range(self.height):
                for x in range(self.lenght):
                    color = self.inspect_pixel_coordinate(y, x)
                    ppm_file.write(f'{color.r} {color.g} {color.b} ')
                ppm_file.write('\n')
                



        