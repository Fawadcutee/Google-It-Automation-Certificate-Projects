#!/usr/bin/env python3

#Google IT Automation with python professional Certificate
#Muhammad Fawad Rahim
#3 Feb, 2021

import email.message
import mimetypes
import smtplib
import os




'''creates an email with an attachment'''
def generateEmail(sender,recipient,subject,body,attachment_path):
    #basic Email Formatting
    message = email.message.EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    #process the attachment and add it to Email
    attachment_filename = os.path.basename(attachment_path)
    mimetype, _ = mimetypes.guess_type(attachment_path)
    mimetype, mime_subtype = mimetype.split('/',1)

    with open(attachment_path, 'rb') as openedfile:
        message.add_attachment(openedfile.read(), maintype = mimetype, subtype = mime_subtype, filename = attachment_filename)

    return message

def generate_error_report(sender,recipient,subject,body):
    #basic Email Formatting
    message = email.message.EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    return message





def sendEmail(message):
    '''sends the message/email to the configured smtp server'''
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
