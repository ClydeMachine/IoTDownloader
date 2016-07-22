import boto3

# This should be initiated via Lambda!

def handler(event,context):
    s3client = boto3.client('s3')
    s3 = boto3.resource('s3')
    object = s3.Bucket('repoabr').Object('fileurl.txt')

    if(event['clickType']=='SINGLE'):
        signedUrl = s3client.generate_presigned_url(
            ClientMethod='get_object',
            ExpiresIn='300',
            Params={
                'Bucket': 'repoabr',
                'Key': '1.mp3'
            }
        )
        object.put(Body=signedUrl)

    if(event['clickType']=='DOUBLE'):
        signedUrl = s3client.generate_presigned_url(
            ClientMethod='get_object',
            ExpiresIn='300',
            Params={
                'Bucket': 'repoabr',
                'Key': '2.mp3'
            }
        )
        object.put(Body=signedUrl)

    if(event['clickType']=='LONG'):
        object.put(Body='NO DOWNLOAD FOR YOU')


# Example IoT Button input to Lambda:
# {
#        "serialNumber": "G030JF0512956M2Q",
#        "clickType": "SINGLE",
#        "batteryVoltage": "2000 mV"
# }

# Build into a bundle with:
# zip -r bundle.zip iotdownloader.py !make sure you use "iotdownloader.handler" as the Lambda function handler!
# zip -r9 bundle.zip /usr/lib/python2.7/site-packages/* !for external libraries
# Then upload to Lambda, run test, success.