import boto3

rekog= boto3.client('rekognition')

photo = 'actress.jpg'
response = rekog.recognize_celebrities(
    Image={
        'S3Object': {
            'Bucket': 'hallymbucket',
            'Name': photo,
        }
    }
)
print("Detected faces for", photo)
for celebrity in response['CelebrityFaces']:
    print ('Name: ' + celebrity['Name'])