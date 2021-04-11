import boto3

s3 = boto3.resource('s3')

response = s3.create_bucket(
    Bucket='hallymbucket'
)
print(response)