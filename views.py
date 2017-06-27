from django.shortcuts import render
import kairos_face
import psycopg2
from django import db
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import json
from django.shortcuts import *
from django.template import RequestContext
from django.http import JsonResponse
import logging
from django.db import connection


# Create your views here.
def enroll(request):
	try:
		cur = connection.cursor()
		logging.info('DB connected')
	except:
		logging.info('Db connection error')
		
		
	kairos_face.settings.app_id = 'Your APP ID'
	kairos_face.settings.app_key = 'Your App key'
	
	if request.method == 'POST':
			#POST goes here . is_ajax is must to capture ajax requests.
		if request.is_ajax():
			uname = request.POST.get('uname')
				
			gallery = request.POST.get('gallery')
			image = request.POST.get('image')
			
			try:
				kairos_face.enroll_face(file=image, subject_id=uname, gallery_name=gallery)
				result = 'success'
			except:
				print('Coudn\'t Enroll! Try again')
				result = 'Error'
				
			data = {'uname': uname, 'gallery': gallery, 'result':result}
		
			return JsonResponse(data)
		
	return render(request,'enroll.html')
	
	
def recognize(request):
	try:
		cur = connection.cursor()
		logging.info('DB connected')
	except:
		logging.info('Db connection error')
		
	kairos_face.settings.app_id = 'Your  App ID'
	kairos_face.settings.app_key = 'Your App key'
	
	if request.method == 'POST':
			#POST goes here . is_ajax is must to capture ajax requests.
		if request.is_ajax():
			
				
			gallery = request.POST.get('gallery')
			image = request.POST.get('image')
			
			
			try:
				recognized_faces = kairos_face.recognize_face(file=image, gallery_name=gallery)
				uname = recognized_faces['images'][0]['candidates'][0]['subject_id']
				result = 'success'
			except:
				result = 'error'
				uname = ''
			
			if result == 'success':
				cur.execute(''' select * from cv where uname=%s''',(uname,));
				res = cur.fetchall()
				newlist = [ele for ele in res[0]]
				email = str(newlist[1])
				designation = str(newlist[3])
				team  = str(newlist[4])
				qresult = 'success'
			else:
				qresult = 'error'
				email = ''
				designation = ''
				team = ''
					
			detected_faces = kairos_face.detect_face(file=image)
			gen = detected_faces['images'][0]['faces'][0]['attributes']['gender']['type']
			age = detected_faces['images'][0]['faces'][0]['attributes']['age']
			gender = ''
			if gen == 'M':
				gender=  'Male'
			else:
				gender= 'Female'
				
			
			
			
			

			
			data = {'uname': uname, 'email': email, 'designation':designation, 'team':team, 'result':result, 'qresult':qresult, 'gender': gender, 'age': age}
			return JsonResponse(data)
		
	return render(request,'recognize.html')
