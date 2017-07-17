# kairosvisionapi-python
Implementation of Employee Face recognition system in Python/Django using Kairos API

A. Requirements:

1.Install kairos_face module

2.Django 1.8+

3.DB - Mysql/Postgres

4.Get Api keys at https://developer.kairos.com/signup

5.Create a table with basic employee details in DB.

B. Setting up api keys:

import kairos_face
kairos_face.settings.app_id = 'Your APP ID'
kairos_face.settings.app_key = 'Your App Key'


C. Enrolling Employee details:

kairos_face.enroll_face(file=image, subject_id=uname, gallery_name=gallery)

Recognizing Employee face:

recognized_faces = kairos_face.recognize_face(file=image, gallery_name=gallery)

D. Accessing db:

Update the code in recognize function based on your employee table
