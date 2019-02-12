from PIL import ImageFile, Image

##Put the image you want to look at
imageFilePath = "mes2zwsqv3101.jpg"

##This works by having (r',g',b') = M (r, g, b)
##Where M is a color mixing matrix, r,g,b is a vector of the color components and r',g',b' are the new color values

##Color blindness matrices
Types={
    "Normal_Colour_vision":                     [x[i] for x in map(lambda k: [k[0]/100, k[1]/100, k[2]/100,0.0], [[100, 0, 0],[0, 100, 0], [0, 0, 100]]) for i in range(4)],
    "Red_Blind_Protanopia":                     [x[i] for x in map(lambda k: [k[0]/100, k[1]/100, k[2]/100,0.0], [[56.667, 43.333, 0], [55.833, 44.167, 0], [0, 24.167, 75.833]]) for i in range(4)],
    "Red_Weak_Protanomaly":                     [x[i] for x in map(lambda k: [k[0]/100, k[1]/100, k[2]/100,0.0], [[81.667, 18.333, 0], [33.333, 66.667, 0], [0, 12.5, 87.5]])for i in range(4)],
    "Green_Blind_Deuteranopia":                 [x[i] for x in map(lambda k: [k[0]/100, k[1]/100, k[2]/100,0.0], [[62.5, 37.5, 0], [70, 30, 0], [0, 30, 70]]) for i in range(4)],
    "Green_Weak_Deuteranomaly":                 [x[i] for x in map(lambda k: [k[0]/100, k[1]/100, k[2]/100,0.0], [[80, 20, 0], [25.833, 74.167, 0], [0, 14.167, 85.833]]) for i in range(4)],
    "Blue_Blind_Tritanopia":                    [x[i] for x in map(lambda k: [k[0]/100, k[1]/100, k[2]/100,0.0], [[95, 5, 0], [0, 43.333, 56.667], [0, 47.5, 52.5]]) for i in range(4)],
    "Blue_Weak_Tritanomaly":                    [x[i] for x in map(lambda k: [k[0]/100, k[1]/100, k[2]/100,0.0], [[96.667, 3.333, 0], [0, 73.333, 26.667], [0, 18.333, 81.667]]) for i in range(4)],
    "Monochromacy_Achromatopsia":               [x[i] for x in map(lambda k: [k[0]/100, k[1]/100, k[2]/100,0.0], [[29.9, 58.7, 11.4], [29.9, 58.7, 11.4], [29.9, 58.7, 11.4]]) for i in range(4)],
    "Blue_Cone_Monochromacy_Achromatomaly":     [x[i] for x in map(lambda k: [k[0]/100, k[1]/100, k[2]/100,0.0], [[61.8, 32, 6.2], [16.3, 77.5, 6.2], [16.3, 32.0, 51.6]]) for i in range(4)]
}

##Open the image and convert it to RGB
image=Image.open(imageFilePath)
image=image.convert("RGB")

for k, v in Types.items():
    ##This converts the images to RGB applying the color matrix matrices
    temp=image.convert("RGB",v)
    temp.save(k+".png")


