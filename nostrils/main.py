import numpy as np
import cv2

#flag = [i for i in dir(cv2) if i.startswith('COLOR_')]
#print(flag)

cap = cv2.VideoCapture(0)

while(1):
	_, frame = cap.read() #returns src, value. don't care about value, so use _ or butts, doesn't really matter

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #
	#hsv = cv2.cvtColor(frame,cv2.COLOR_YUV2BGRA_Y422)	

	lower_blue = np.array([110,50,50]) #similiar to matlab, literally an array with 3 elements
	upper_blue = np.array([130,255,255])

	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	res = cv2.bitwise_and(frame,frame,mask = mask) #mask chooses the elements to be swapped

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
