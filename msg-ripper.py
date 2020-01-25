#!/usr/bin/env python
# coding: utf-8

import os
import extract_msg
from datetime import datetime
import hashlib
import iocextract

now = datetime.now()
currtime = now.strftime("%d-%b-%Y %H:%M:%S")
timestampStr = now.strftime("%d_%b_%Y_%H_%M_%S")
print("Script started: ",currtime)


def sanitizeUrl(url):
    url = url.replace("http", "hxxp").replace(".", "[.]").replace(':', '[:]')
    return url
#resultsDir = './'+timestampStr+'_testrun'
# create folder to output results in 
#createFolder('./'+timestampStr+'_testrun')




samplesDir = "./samples"
sCounter = 0
# Iterate over .msg files in the folder
for subdir, dirs, files in os.walk(samplesDir):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".msg"):
            #print (filepath)
            sCounter += 1
            msg = extract_msg.Message(filepath)
            print("Sample {}: {}".format(sCounter, msg.filename))
            print("Date: ",msg.date)
            print("Sender: ",msg.sender)
            print("To: ",msg.to)
            print("Reply To: ",msg.reply_to)
            print("Subject: ",msg.subject)
            # Extract URL IOCs
            if msg.body:
                urls = list(iocextract.extract_urls(msg.body))
                urlCounter = 0
                print("URLs:", len(urls))
                for urlioc in urls:
                    urlCounter += 1
                    print("  {}> {}".format(urlCounter, sanitizeUrl(urlioc)))
            print("Attachments: ",len(msg.attachments))
            # Iterate over attachments
            attchCounter = 0
            for attch in msg.attachments:
                attchCounter += 1
                print("Attachment #{}:".format(attchCounter))
                if type(attch.data) == extract_msg.message.Message:
                    subMsg = msg.attachments[0].data
                    print("> Attachment is an Email:")
                    print("    Date: ",subMsg.date)
                    print("    Sender: ",subMsg.sender)
                    print("    To: ",subMsg.to)
                    print("    Reply To: ",subMsg.reply_to)
                    print("    Subject: ",subMsg.subject)
                    if subMsg.body:
                        urls = list(iocextract.extract_urls(subMsg.body))
                        urlCounter = 0
                        print("    URLs:", len(urls))
                        for urlioc in urls:
                            urlCounter += 1
                            print("    {}> {}".format(urlCounter, sanitizeUrl(urlioc)))
                    print("    Attachments: ",len(subMsg.attachments))
                    subAttchCounter = 0
                    for subattch in subMsg.attachments:
                        sep = "+"*50
                        print("   ", sep)
                        subAttchCounter += 1
                        print("    Sub Attachment #{}:".format(subAttchCounter))
                        attchdata = subattch.data
                        md5sum = hashlib.md5(attchdata).hexdigest()
                        sha1sum = hashlib.sha1(attchdata).hexdigest()
                        print("    Attachment Short File Name: ", subattch.shortFilename)
                        print("    Attachment Long File Name: ", subattch.longFilename)
                        print("    MD5 Hash: ",md5sum)
                        print("    SHA1 Hash: ",sha1sum)
                else:
                    md5sum = hashlib.md5(attch.data).hexdigest()
                    sha1sum = hashlib.sha1(attch.data).hexdigest()
                    print("Attachment Short File Name: ", attch.shortFilename)
                    print("Attachment Long File Name: ", attch.longFilename)
                    print("MD5 Hash: ",md5sum)
                    print("SHA1 Hash: ",sha1sum)
                

#             msg.save(customPath=resultsDir)
            print("="*60)
