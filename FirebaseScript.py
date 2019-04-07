import urllib.request
import cv2
import numpy as np
import os
import pyrebase

def initialize():

	config = {
	    "apiKey": "AIzaSyBeX0KqTpVD3MR-L9loT-5A-tn7vzM4K3Y",
	    "authDomain" : "voidhacks-b9a68.firebaseapp.com",
	    "databaseURL" : "https://voidhacks-b9a68.firebaseio.com",
	    "projectId" : "voidhacks-b9a68",
	    "storageBucket" : "voidhacks-b9a68.appspot.com",
	    "messagingSenderId" : "1006738360390"
	}
	firebase = pyrebase.initialize_app(config)

	db = firebase.database()

    #firebase1 = firebase.FireBaseApplication("https://voidhacks-b9a68.firebaseio.com")

    #firebase1.post('/user11',('name':'arshit'))

	content_link=db.child('ImagePath').child('imageUri').get().val()

	urllib.request.urlretrieve(content_link, "Content1"+".jpeg")

	mixed_image = cv2.imread('FinalImage.jpg')

	#db.child('ImagePath').child('MixedImage').push(mixed_image)



initialize()