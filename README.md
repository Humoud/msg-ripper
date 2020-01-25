# msg-ripper
For bulk analysis of msg files

note: this is still a work in progress

### Requirements
* Python 3.7
* [extract_msg](https://github.com/mattgwwalker/msg-extractor)
* [iocextract](https://github.com/InQuest/python-iocextract)

### Usage
The script iterates over a .msg files in the specified folder and does the following:
 * Extract the date, sender, receiver, reply to, and subject header
 * Extract URLs from the body of the email and attachments of type email
 * Generate MD5 and SHA1 hashes for the attachments and sub attachments

The script is best used in a jupyter notebook(will upload one later) for interactive analysis. Modify variable `samplesDir` to point to the directory which contains the .msg files.

The following is what to expect from the output. I am running the script from the command line for the sake of showing what the script outputs:
```bash
$ python3.7 msg_phish.py 
Script started:  25-Jan-2020 20:59:37
Sample 1: ./samples/EMAILNAME.msg
Date:  Wed, 22 Jan 2020 16:28:46 +0300
Sender:  SENDEREMAIL
To:  RECVEMAIL
Reply To:  None
Subject:  SUBJECT
URLs: 3
  1> hxxps[:]//RANDOM[.]URL[.]IOC[.]net
  2> hxxps[:]//RANDOM[.]URL[.]IOC[.]net
  3> hxxps[:]//RANDOM[.]URL[.]IOC[.]net
Attachments:  2
Attachment #1:
Attachment Short File Name:  File~1.jpe
Attachment Long File Name:  FILENAME.jpeg
MD5 Hash:  MD5HASH
SHA1 Hash:  SHA1HASH
Attachment #2:
Attachment Short File Name:  File~1.pdf
Attachment Long File Name:  FILENAME.pdf
MD5 Hash:  MD5HASH
SHA1 Hash:  SHA1HASH
============================================================
Sample 2: ./samples/EMAILNAME2.msg
Date:  Thu, 18 Oct 2018 17:21:29 +0300
Sender:  SENDEREMAIL
To:  RECVEMAIL
Reply To:  None
Subject:  SUBJECT 
URLs: 0
Attachments:  1
Attachment #1:
> Attachment is an Email:
    Date:  Thu, 18 Oct 2018 17:10:51 +0300
    Sender:  SENDEREMAIL
    To:  RECVEMAIL
    Reply To:  None
    Subject:  SUBJECT
    Attachments:  1
    ++++++++++++++++++++++++++++++++++++++++++++++++++
    Sub Attachment #1:
    Attachment Short File Name:  FILENAME.txt
    Attachment Long File Name:  FILENAME.txt
    MD5 Hash:  MD5HASH
    SHA1 Hash:  SHA1HASH
```
