import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Specify the bucket name
bucket_name = 'static-cloud-wallet'


s3.put_object(Bucket='static-cloud-wallet', Key='index.html', Body=bodyOfFileGoesHere, ContentType='text/html')