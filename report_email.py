#!/usr/bin/env python3

#Google IT Automation with python professional Certificate
#Muhammad Fawad Rahim
#3 Feb, 2021

import email.message
import mimetypes
import smtplib
import os
import reports
import datetime
import json
import emails


#description_location = os.path.expanduser('~') + '/supplier-data/descriptions/'
#description_location = 'supplier-data/descriptions/'
description_location = 'E:/testtxt/'
report = []



def process_dateformat():
    format_date = datetime.datetime(2021, 2, 1)
    month = format_date.strftime("%B")
    day = str(format_date.day)
    year = str(format_date.year)
    title = 'Processed Update on ' + month + day + "," + year

    return title



def process_data(description_location):
    all_text_data = []
    for file in os.listdir(description_location):
        if os.path.exists(description_location + file):
            with open(description_location + file , 'r') as openedfile:
                all_text_data.append([line.strip() for line in openedfile.readlines()])


    print(all_text_data)

    return all_text_data


def process_again_data(data_list):
    for item in data_list:
        report.append("name: {} <br/> weight: {}\n".format(item[0],item[1]))

    return report



def main():
    #attachment_path = '/tmp/Processed.pdf'
    attachment_path = 'E:/Processed.pdf'
    title = process_dateformat()
    data_list = process_data(description_location)
    bodytext = process_again_data(data_list)
    paragraph = '<br/><br/>'.join(bodytext)

    ''' we are going to call the generate_report method from resports module to generate a pdf '''
    reports.generate_report(attachment_path,title,paragraph)


    sender = 'automation@example.com'
    recipient = 'student-01-9067a0c1f76d@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'


    ''' we are going to generate an email by calling the generateEmailmethod from emails module '''
    message = emails.generateEmail(sender,recipient,subject,body,attachment_path)
    print(message)



    ''' send email by calling sendEmail method from emails module '''
    #emails.sendEmail(message)


if __name__ == '__main__':
    main()
