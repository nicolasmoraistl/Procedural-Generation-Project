with open('python_scripts/pamphilemayatristanmargaux.ppm', 'r') as test:
    idk = test.read()
    splitted_idk = idk.split(' ')
    print(len(splitted_idk))
    print(idk[12])