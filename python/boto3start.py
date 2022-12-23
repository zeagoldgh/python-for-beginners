import boto3
region = "us-west-2"
s3_client = boto3.client("s3", region_name = "us-west-2")
location = {'LocationConstraint': region}
s3_client.create_bucket(Bucket = 'wale-buck-for-boto3',CreateBucketConfiguration = location)