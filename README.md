# kairosvisionapi-python
Implementation of Employee Face recognition system in Python/Django using Kairos API

Requirements:

Install kairos_face
Get Api keys at https://developer.kairos.com/signup

Create a table in Postgress DB with employee details

Setting up api keys:

import kairos_face
kairos_face.settings.app_id = 'Your APP ID'
kairos_face.settings.app_key = 'Your App Key'


Enrolling Employee details:

kairos_face.enroll_face(file=image, subject_id=uname, gallery_name=gallery)

Recognizing Employee face:

recognized_faces = kairos_face.recognize_face(file=image, gallery_name=gallery)

Accessing db:

Update the code in recognize function based on your employee table
