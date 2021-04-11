import boto3

s3 = boto3.resource('s3')

s3.meta.client.upload_file('./img/actor.jpg', 'hallymbucket', 'actor.jpg')
s3.meta.client.upload_file('./img/actress.jpg', 'hallymbucket', 'actress.jpg')
s3.meta.client.upload_file('./img/img-text.jpg', 'hallymbucket', 'img-text.jpg')
s3.meta.client.upload_file('./img/alright.jpg', 'hallymbucket', 'alright.jpg')