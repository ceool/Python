import boto3

# account_id = boto3.client('sts').get_caller_identity().get('Account')
# print('Account ID:', account_id)

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)