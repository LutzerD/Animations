cap = cv2.VideoCapture(0)

while(1):
	_, frame = cap.read() #returns src, value. don't care about value, so use _ or butts, doesn't really matter
        
	cv2.imshow('res',cv2.canny(frame,100,200))

        
        
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
	if h < hmax:
		h = h + 1;
	else:
		h = hmin;

	cv2.destroyAllWindows()
