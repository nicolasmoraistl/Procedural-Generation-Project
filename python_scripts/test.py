import palette_code
import image_generator

palette = palette_code.Colorset('python_scripts/cores.hex')

print(palette.check_amount_of_colors())

palette.add_color_to_colorset(palette_code.RGB(5, 123, 44))

print(palette.check_amount_of_colors())

print(palette.colorset)

img = image_generator.Image(3, 2)

img.open_ppm_file('python_scripts/imagem.ppm')

print(img.inspect_pixel_coordinate(0, 0).r)


