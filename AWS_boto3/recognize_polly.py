import boto3

def polly_sentence(sentence):
    file_name = 'speech.mp3'
    polly_client = boto3.Session(
        aws_access_key_id='key',                     
        aws_secret_access_key='key',
        aws_session_token='token',
        region_name='us-east-1').client('polly')

    response = polly_client.synthesize_speech(VoiceId='Joanna', OutputFormat='mp3', Text = sentence)

    file = open(file_name, 'wb')
    file.write(response['AudioStream'].read())
    file.close()
    print('Audio output: ', file_name)


def detect_text(photo, bucket, name):
    client=boto3.client('rekognition')
    sentence = ''

    print ("Analying image [{}] ...".format(photo), end='')
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
                        
    textDetections=response['TextDetections']
    print('done:')
    for text in textDetections:
        if 'ParentId' in text:
            continue
        sentence += text['DetectedText'] + ' '
    print('sentence found : ', sentence)
    sentence += name

    return sentence

def main():
    bucket = 'hallymbucket'
    photo = 'alright.jpg'
    name = 'JoonHyun Park'
    polly_sentence(detect_text(photo, bucket, name))
    
if __name__ == "__main__":
    main()