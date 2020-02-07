from PIL import Image
import os
from pylab import *
import re
from PIL import Image, ImageChops, ImageEnhance
#def finalfun(path):
    #return path
    #def get_imlist(path):
        #return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.png')]
def convert_to_ela_image(path, quality = 90):
    filename = path
    resaved_filename = filename.split('.')[0] + '.resaved.jpg'
    ELA_filename = filename.split('.')[0] + '.ela.png'
    
    im = Image.open(filename).convert('RGB')
    im.save(resaved_filename, 'JPEG', quality=quality)
    resaved_im = Image.open(resaved_filename)
    
    ela_im = ImageChops.difference(im, resaved_im)
    
    extrema = ela_im.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1
    scale = 255.0 / max_diff
    
    ela_im = ImageEnhance.Brightness(ela_im).enhance(scale)
    
    #return ela_im
    #ela_img = convert_to_ela_image(path,90)
    black=0
    others=0
    w,h=ela_im.size
    #print(w,h)
    pixLocation = [(y, x) for x in range(h) for y in range(w)]
    pixRGB = list(ela_im.getdata())
    #print (len(pixRGB))
    #print(pixRGB)
    for pixel in pixRGB:
        if pixel == (0, 0, 0):
            black += 1
        else:
            others += 1
    #print(black)
    #print(others)
    #print(len(pixel))
    x = ((len(pixRGB)-black)/len(pixRGB))*100
    # if x>=40:
    #     return 1
    # else:
    #     return 0
    return round(x, 3)

# print(convert_to_ela_image('morphtest2.jpg'))