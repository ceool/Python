import boto3

name = 'hallymbucket'
s3 = boto3.client('s3')
print("Listing objects in my bucket: ", name)
for key in s3.list_objects(Bucket=name)['Contents']:
    print("　", key['Key'])