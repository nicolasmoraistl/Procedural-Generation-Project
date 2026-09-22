import image_generator, palette_code



flag = image_generator.Image(300, 200)


for row in range(flag.height):
    for column in range(flag.lenght):
        if column < 99:
            flag.define_pixel_color(row, column, palette_code.RGB(0, 0, 145))
        elif column > 99 and column < 199:
            flag.define_pixel_color(row, column, palette_code.RGB(255, 255, 255))
        else:
            flag.define_pixel_color(row, column, palette_code.RGB(225, 0, 15))

flag.save_ppm_image('python_scripts/flags/france.ppm')

for row in range(flag.height):
    for column in range(flag.lenght):
        if row < 99:
            flag.define_pixel_color(row, column, palette_code.RGB(0, 87, 183))
        else:
            flag.define_pixel_color(row, column, palette_code.RGB(255, 215, 0))

flag.save_ppm_image('python_scripts/flags/ukraine.ppm')

for row in range(flag.height):
    for column in range(flag.lenght):
        if row < 68:
            flag.define_pixel_color(row, column, palette_code.RGB(174, 28, 40))
        elif row > 67 and row < 134:
            flag.define_pixel_color(row, column, palette_code.RGB(255, 255, 255))
        else:
            flag.define_pixel_color(row, column, palette_code.RGB(33, 70, 139))

flag.save_ppm_image('python_scripts/flags/netherlands.ppm')




