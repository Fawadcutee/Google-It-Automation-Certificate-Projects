import os
import requests

'''
List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.
Hint: Use os.listdir() method for this, which returns a list of all files and directories in the specified path.
'''
dir = 'E:/testtxt/'
for file in os.listdir(dir):
    '''
    You should now have a list that contains all of the feedback files from the path /data/feedback.
    Traverse over each file and, from the contents of these text files, create a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively.
    '''
    format = ["title","name","date","feedback"]

    '''
    Now, you need to have a dictionary with keys and their respective values (content from feedback files).
    This will be uploaded through the Django REST API.
    '''
    content = {}

    with open('{}/{}'.format(dir,file), 'r') as txtfile:
        counter = 0
        for line in txtfile:
            line = line.replace("\n", "")
            content[format[counter]] = line.strip('\n')
            counter += 1


print(content)
