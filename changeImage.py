#!/usr/bin/env python3

#Google IT Automation with python professional Certificate
#Muhammad Fawad Rahim
#3 Feb, 2021

from PIL import Image
import os


''' processing image to change its size and extension within same directory'''
def process_image(imagespath):
    for file in os.listdir(imagespath):
        if file.endswith('.tiff'):
            image_object = Image.open(imagespath + file)
            filename, extension = os.path.splitext(imagespath + file)
            rgb_image_object = image_object.convert("RGB")
            new_image_object = rgb_image_object.resize((600,400))
            new_image_object.save(filename + '.jpeg', "jpeg", quality=90)




def main():
    #imagesdirectorypath = os.path.expanduser('~') + '/supplier-data/images/'
    imagesdirectorypath = 'supplier-data/images/'
    if os.path.exists(imagesdirectorypath):
        process_image(imagesdirectorypath)
    else:
        print("path didn't exist")



if __name__ == "__main__":
    main()
