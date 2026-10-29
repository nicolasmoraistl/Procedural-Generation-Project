import image_generator

flag = image_generator.Image(60, 40)

flag.open_ppm_file('python_scripts/flags/netherlands.ppm')

flag.save_ppm_image('python_scripts/flags/netherlands_resized.ppm')

