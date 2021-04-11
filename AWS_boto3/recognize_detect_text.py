import boto3

def detect_text(photo, bucket):
    client=boto3.client('rekognition')

    print ("Analying image...", end='')
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}},
        Filters={'WordFilter':{'MinConfidence':1}})
                        
    textDetections=response['TextDetections']
    print('done:')
    for text in textDetections:
        if 'ParentId' in text:
            if text['ParentId'] != 0:
                continue
        if text['Confidence'] > 99:
            print ('　Text found: ' + text['DetectedText'])


def main():
    bucket='hallymbucket'
    photo='img-text.jpg'
    detect_text(photo,bucket)

if __name__ == "__main__":
    main()