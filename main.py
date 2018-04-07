# I will be using Amazon SDK for Python (Boto)
import boto3

import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("python-cam-capture")

img_counter = 0

while True:
    if img_counter == 2:
        break
    ret, frame = cam.read()
    cv2.imshow("python-cam-capture", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "rekognition_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

    



with open("rekognition_0.png", "rb") as imageFile:
    f = imageFile.read()
    str1 = bytearray(f)

with open("rekognition_1.png", "rb") as imageFile:
    f = imageFile.read()
    str2 = bytearray(f)

client = boto3.client('rekognition', region_name='us-west-2')
# pdb.set_trace()
try:
    response = client.compare_faces(
        SourceImage={
            'Bytes': str1,
            # 'S3Object': {
            #     'Bucket': 'shariqueme',
            #     'Name': 'sharique1.jpg',
            # 'Version': 'string'
            # }
        },
        TargetImage={
            'Bytes': str2,
            # 'S3Object': {
            #     'Bucket': 'shariqueme',
            #     'Name': 'sharique3.jpg',
            #     # 'Version': 'string'
            # }
        },

        SimilarityThreshold=25
    )

    print(response)
    try:

        a = response['FaceMatches']
        t = a[0]
        print('face matches ' + str(t['Similarity']) + ' percent')
    except:
        print("source and target images don't have any similar faces")
except Exception as e:
    print("Invalid parameters", e)


