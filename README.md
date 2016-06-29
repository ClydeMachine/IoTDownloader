# IoTDownloader

IoT-enabled download gate. 

Using an AWS IoT button, you can generate a temporary presigned S3 URL for a time-locked exclusive download of ome or two files you have in your S3 bucket. Singlepress the button to generate a URL for the first file, or doublepress for the second file, and longpress the button to remove the URL. Made primarily for musicians who want to offer an exclusive download of a song or album from S3, and be able to trigger this while out and about (i.e. on stage at a show). 

# Requirements

Boto3.

Naturally this will also require a triggering action to run (AWS IoT button is used for this project), and you will need to set up both a webserver for the webpage portion, as well as implement the iotdownloader.py script in AWS Lambda.

