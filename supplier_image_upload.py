#!/usr/bin/env python3

#Google IT Automation with python professional Certificate
#Muhammad Fawad Rahim
#3 Feb, 2021

import os
import requests


''' this method will upload files from a directory to a web server using python requests module'''
def uploadImagefiles (filespath):
    url = 'http://localhost/upload/'
    for file in  os.listdir(filespath):
        if os.path.exists(filespath + file):
            if file.endswith('.jpeg'):
                with open(filespath + file, 'rb') as openedfile:
                    response = requests.post(url, files={'file' : openedfile})
                    #if not response.ok:
                        #raise Exception("GET failed with status code {}".format(response.status_code))




def main():
    filespath = 'supplier-data/images/'
    uploadImagefiles(filespath)




if __name__ == '__main__':
    main()
