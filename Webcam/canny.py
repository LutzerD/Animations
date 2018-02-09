import numpy as np
import cv2
import random

#flag = [i for i in dir(cv2) if i.startswith('COLOR_')]
#print(flag)

cap = cv2.VideoCapture(0)
_, frame_old = cap.read() #returns src, value. don't care about value, so use _ or butts, doesn't really matter
#frame_old = cv2.Canny(frame_old,100,200)
alpha_min = .9
alpha_max = .95
alpha_delta = .001
alpha = alpha_min

ascending = True

while(1):

 #       alpha = random.uniform(alpha_min, alpha_max)
        
        _, res = cap.read() #returns src, value. don't care about value, so use _ or butts, doesn't really matter
        #res = cv2.Canny(res,100,200)

        cv2.addWeighted(frame_old, alpha, res, 1 - alpha,0, res)        
        cv2.imshow('res' + str(alpha),res)
        
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
                break
        cv2.destroyAllWindows()

        frame_old = res
        
        if(not ascending and alpha-alpha_delta > alpha_min):
                alpha = alpha-alpha_delta
        elif (not ascending and alpha-alpha_delta <= alpha_min):
                ascending = True
                alpha = alpha + alpha_delta
        elif(ascending and alpha+alpha_delta < alpha_max):
                alpha = alpha+alpha_delta
        elif (ascending and alpha+alpha_delta >= alpha_min):
                ascending = False
                alpha = alpha - alpha_delta
        else:
                print("Broken at:" + str(ascending) + ", " + str(alpha))
