import boto3

def recognize_celebrities(img_dir, photo):
    rekog=boto3.client('rekognition')

    with open(img_dir+photo, 'rb') as image:
        response = rekog.recognize_celebrities(Image={'Bytes': image.read()})

    print('Detected faces for ' + photo)    
    for celebrity in response['CelebrityFaces']:
        print ('Name: ' + celebrity['Name'])

def main():
    img_dir = './img/'
    photo = 'actor.jpg'
    recognize_celebrities(img_dir, photo)

if __name__ == "__main__":
    main()