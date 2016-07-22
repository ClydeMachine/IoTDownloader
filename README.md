# IoTDownloader

[![ScreenShot](http://i.imgur.com/gJeRBhU.png)](https://youtu.be/N_EoBP7sU2A)

IoT-enabled download gate. 

Using an AWS IoT button, you can generate a temporary presigned S3 URL for a time-locked exclusive download of one or two files you have in your S3 bucket. Singlepress the button to generate a URL for the first file, or doublepress for the second file, and longpress the button to remove the URL from the page altogether. Made primarily for musicians who want to offer an exclusive download of a song or album from S3, and be able to trigger this whenever while out and about (i.e. on stage at a show giving an exclusive download for attendees-only). 

# Requirements

- Python 2.7

- Boto3

- AWS account for Lambda function

Naturally this project will also require a triggering action to run (AWS IoT button, specifically), and you will need to set up both a webserver for the webpage portion, as well as implement the iotdownloader.py script in AWS Lambda.

In short, the structure is:

- Put all the contents of /var/www on a webserver running Apache.
- Update the Python code in the Lambda folder to point to a bucket of your own and at least one file within it.
- Put the Python code into Lambda by means of making a bundle.zip file that includes boto3. There are tutorials on how to do this. Make sure the handler is set to "iotdownloader.handler".
- Naturally, make sure the Lambda function has an appropriate IAM role assigned to it that will allow reads and writes to the bucket of your choosing.
- Set up your AWS IoT button to be the Event Source for the Lambda function, and you should be good to go.

If that sounds like a lot of steps, it is if it's your first time using any of the above. But, I got mine running in under a half hour, for what that's worth.
