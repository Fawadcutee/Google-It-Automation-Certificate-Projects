#!/usr/bin/env python

#Google IT Automation with python professional Certificate
#Muhammad Fawad Rahim
#3 Feb, 2021

import shutil
import psutil
import os
#import emails
import socket

"""Verifies that there's enough free space on disk"""
def check_disk_usage(disk):
    disk_usage = shutil.disk_usage(disk)
    percentage = disk_usage.free/disk_usage.total*100
    return percentage > 20

"""check localhost is correctly configured on 127.0.0.1"""
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'


"""Verifies that there's enough unused CPU"""
def check_cpu_usage():
    cpu_usage =psutil.cpu_percent(1)
    return cpu_usage < 80

def check_memory_usage():
    available_memory=psutil.virtual_memory().available/(1024*1024)
    return available_memory >500

error = False
to_be_checked = {check_cpu_usage() : "CPU usage is over 80%", check_localhost():"localhost cannot be resolved to 127.0.0.1", check_disk_usage("/") : "Available disk space is less than 20%", check_memory_usage(): "Available memory is less than 500MB"}

for action, error in to_be_checked.items():
    if not action:
        error_summary = error
        print(error_summary)

        error = True



if error:
    try:
        sender = "automation@example.com"
        recipient = "@example.com"
        subject = "Error - {}".format(error_summary)
        body = "Please check your system and resolve the issue as soon as possible"
        message =  emails.generate_report(sender,recipient,subject,body)
        #emails.sendEmail(message)
        print(message)
    except Exception as e:
        print(e)
