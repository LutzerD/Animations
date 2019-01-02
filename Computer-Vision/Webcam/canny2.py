import numpy as np
import cv2
import random
import imageio
from matplotlib import pyplot as plt

##cap = cv2.VideoCapture(0)
##_, frame_old = cap.read()

filename = 'Sample.mp4'
vid = imageio.get_reader(filename,  'ffmpeg')

#alpha = alpha_min
alpha = .9
ascending = True

frame_old = vid.get_data(1)
x,y,z = frame_old.shape
print(x)
print(y)
print(z)

dx = round(x*.55)
offset = round(x*.01)

##while(1):
        ##_, frame = cap.read()
for i in range(2,len(vid)):
        frame = vid.get_data(i)        
        #frame_mod[x-dx+offset:,:,:] = frame_old[x-dx:-offset,:,:].copy()

 #       img = cv2.cvtColor(frame_mod,cv2.COLOR_BGR2GRAY)
        #img = cv2.resize(cv2.medianBlur(frame,5), None, fx=0.5, fy=0.5)
        img = cv2.cvtColor(cv2.medianBlur(frame,5), cv2.COLOR_RGB2GRAY)
        frame_mod = cv2.Canny(img, 30,100)

        kernel = np.ones((5,5),np.uint8)
 #       frame_mod = cv2.morphologyEx(frame_mod, cv2.MORPH_CLOSE, kernel)
 #       frame_mod = cv2.dilate(frame_mod,kernel,iterations = 1)
        frame_mod = cv2.morphologyEx(frame_mod, cv2.MORPH_CLOSE, kernel)
 #       frame_mod = cv2.morphologyEx(frame_mod, cv2.MORPH_OPEN, kernel)

        cimg = cv2.cvtColor(frame_mod.copy(), cv2.COLOR_GRAY2RGB)
        
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=30,maxRadius=60)
        print(circles)
        try:
                circles = np.uint16(np.around(circles))
                for i in circles[0,:]:
                    # draw the outer circle
                    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
                    # draw the center of the circle
                    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        except:
                c = 1

            
        #cv2.addWeighted(frame_old, alpha, frame, 1 - alpha,0, frame_old)        

        res = cv2.resize(cimg, None, fx=0.5, fy=0.5)
        #res = cv2.cvtColor(res, cv2.COLOR_RGB2BGR)
        #res = cimg.copy()
        ##res = frame_old.copy()

        frame_sized = cv2.resize(frame, None, fx=0.5, fy=0.5)
#        frame_sized = cv2.Canny(frame_sized,50,200)
        #frame_sized = cv2.cvtColor(frame_sized, cv2.COLOR_BGR2RGB)

        ##final= np.concatenate((cv2.Canny(res,100,200), cv2.Canny(frame_sized,100,200)), axis=1)
        print(frame_mod.shape)
        print(frame_old.shape)
        final = np.concatenate((res, frame_sized), axis=1)
        ##res = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)

        


        
        ##final = res
        #cv2.imshow('frame',final)
        cv2.imshow('frame',final)
        frame_old = frame_mod;

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
        	break

        cv2.destroyAllWindows()
