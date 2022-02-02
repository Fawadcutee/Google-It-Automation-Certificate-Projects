#!/usr/bin/env python3

#Google IT Automation with python professional Certificate
#Muhammad Fawad Rahim
#2 Feb, 2021

import os
import requests



# description_location = os.path.expanduser('~') + '/supplier-data/descriptions/'
#description_location = 'supplier-data/descriptions/'
# images_location = os.path.expanduser('~') + '/supplier-data/images/'
#images_location = ''
imageslist = []


''' this method will fetch images from directory and make a sorted list '''
def getimages(imagespath):
    for image in os.listdir(imagespath):
        if os.path.exists(imagespath + image):
            if os.path.isfile(imagespath + image):
                if image.endswith('.jpeg'):
                    imageslist.append(image)
    return sorted(imageslist)


''' this method will process text files from a directory into a json dictionary'''
def processtxtfiles (filespath, imagelist):
    imagecounter = 0
    fruitdict = {}
    #url =
    keys = ['name','weight','description']
    for txtfile in sorted(os.listdir(filespath)):
        if os.path.exists(filespath + txtfile):
            #counter = 0
            with open(filespath + txtfile, 'r') as openedfile:
                #for line in openedfile:
                #    fruitdict[keys[counter]] = line.strip()
                #    if counter != 2:
                #        counter+=1
                #    else:
                #        pass
                contents = openedfile.read().split("\n")[0:3]
                counter = 0
                for content in contents:
                  fruitdict[keys[counter]]= content
                  counter+=1


                temp = fruitdict['weight']
                #print(temp)
                templist = temp.split()
                #print(templist)
                checktype = templist[0]
                #print(checktype)

                weight_int = int(checktype)
                #print(weight_int)
                fruitdict['weight'] = weight_int
                fruitdict['image_name'] = imagelist[imagecounter]
                imagecounter += 1
                print(fruitdict)

                ''' lets call the method which will upload these files '''
                #uploadtxtfiles(fruitdict)



def uploadtxtfiles(fruitdictionary):
    url = 'http://34.66.75.188/fruits/'
    response = requests.post(url, json= fruitdictionary)
    if not response.ok:
        raise Exception("POST failed! | Status code: {} | File: {}".format(response.status_code))
    else:
        print('post Successful')


def main():
    filespath = 'supplier-data/descriptions/'
    imagespath = 'supplier-data/images/'
    #filespath = 'E:/testtxt/'
    #imagespath = 'E:/images/'
    ''' lets get fetch the images first into a list '''
    imagelist = getimages(imagespath)
    ''' going to process text files and make a dictionary and then upload using requests module '''
    processtxtfiles(filespath, imagelist)
    #uploadtxtfiles({"name": "Test Fruit", "weight": 100, "description": "This is the description of my test fruit", "image_name": "icon.sheet.png"})

if __name__ == '__main__':
    main()
