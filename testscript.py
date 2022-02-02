#!/usr/bin/env python3

# Google IT Automation with Python Professional Certificate
# Muhammad Fawad rahim
# 27 Jan 2021

import os
import requests

#feedbackdirectory = os.path.expanduser('~') + '/data/feedback'
feedbackdirectory = '/data/feedback/'
feedbackdictionary = {}
keys = ['title','name','date','feedback']
for file in os.listdir(feedbackdirectory):
    with open(feedbackdirectory + file, 'r') as newfile:
        counter = 0
        for line in newfile:
            feedbackdictionary[keys[counter]] = line.strip()
            counter +=1
    response=requests.post("http://35.225.95.53/feedback/",json = feedbackdictionary)
    if not response.ok:
        raise Exception("POST failed! | Status code: {} | File: {}".format(response.status_code, file))
    else:
        print('Successful Post')
