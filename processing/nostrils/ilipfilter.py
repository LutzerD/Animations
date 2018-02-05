import numpy as np
import cv2

#flag = [i for i in dir(cv2) if i.startswith('COLOR_')]
#print(flag)

#cap = cv2.VideoCapture(0)


hmin = 200;
hmax = 255;
h = hmin;
while(1):
#	_, frame = cap.read() #returns src, value. don't care about value, so use _ or butts, doesn't really matter
	frame = cv2.imread("nose1.jpg")
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #
	#hsv = cv2.cvtColor(frame,cv2.COLOR_YUV2BGRA_Y422)	

	lower_blue = np.array([0,0,0]) #similiar to matlab, literally an array with 3 elements
	upper_blue = np.array([255,250,55])

	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	res = cv2.bitwise_and(frame,frame,mask = mask) #mask chooses the elements to be swapped

	cv2.imshow('frame',np.sort(frame,axis=1))
#	cv2.imshow('mask',mask)
#	cv2.imshow('res, ' + str(h),res)
	
	k = cv2.waitKey(5) & 0xFF

	if k == 27:
		break
	if h < hmax:
		h = h + 1;
	else:
		h = hmin;

	cv2.destroyAllWindows()
