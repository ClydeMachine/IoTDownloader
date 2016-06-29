#!/usr/bin/python

import boto3
import cgi
import cgitb

#
# pullFromS3.cgi
#

s3client = boto3.resource('s3')
fileurlobject = s3client.Object('repoabr','fileurl.txt')
data = fileurlobject.get()["Body"].read().decode("utf-8")

print 'Content-Type: text/html; charset=utf-8\n\n'
print data
