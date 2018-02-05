import numpy as np
import cv2
from matplotlib import pyplot as plt
import math as m

#img = cv2.imread("hotel.jpg") #900,1440,3
#img = cv2.imread("gradient.png") #256,256,3
#img = cv2.imread("Lenna.png") #1080,1920
img = cv2.imread("tron.png")

x,y,z = img.shape
img = cv2.resize(img,(round(y/10)*10, round(x/10)*10),interpolation = cv2.INTER_CUBIC)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
original_shape = np.array(hsv.shape).astype(int)


mask = cv2.inRange(hsv, np.array([0,0,230]), np.array([255,50,255]))
res = cv2.bitwise_and(hsv,hsv,mask = mask)

kernel = np.ones((5,5),np.uint8)
dilation3 = cv2.dilate(res,kernel,iterations = 3)
opening = cv2.morphologyEx(res, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)

#Gross, but i think this is where the for loops come in
row_index = 0;
minimum = 5
row_index = 0
dialationSample = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
original = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

for r in dilation3:
        in_mask = False
        index = 0
        in_mask_counter = 0
        out_mask_counter = 0
        start_indices = []
        stop_indices = []
        print(row_index)
        for c in r:
                #if the value of the cell is >1 and we aren't in mask, hope it hasn't been 1 sample of non-mask or we are just starting.
                #print(str(out_mask_counter) + ',' + str(in_mask_counter))
                #print(c)
                if (c.any() > 0 and in_mask == False):
                    in_mask = True
                    start_indices.append(index)
                    out_mask_counter = 0
                    in_mask_counter = in_mask_counter + 1

                elif(c.all() == 0 and in_mask == True ):
                    in_mask = False
                    stop_indices.append(index)
                    out_mask_counter = out_mask_counter + 1
                    in_mask_counter = 0
                #else:
                    #print("else")
                    
                #keep track of current cell                    
                index = index + 1
                
        #processing the light pairs
        if(len(start_indices) > len(stop_indices)):
            stop_indices.append(start_indices[-1]);
        pair_index = 0
        #print(start_indices)
        for i in start_indices:
                dialationSample[row_index,i-int(minimum*(m.sin(row_index/50)+minimum/2)):stop_indices[pair_index]+int(minimum*(m.sin(row_index/50)+minimum/2)),:] = np.sort(dialationSample[row_index,i-int(minimum*(m.sin(row_index/50)+minimum/2)):stop_indices[pair_index]+int(minimum*(m.sin(row_index/50)+minimum/2)),:], axis=0)
                #print("sorted " + str(row_index) + "," + str(i-minimum) + ":" +str(stop_indices[pair_index] + minimum) + ",:.")
                pair_index+=1
                

        row_index +=1
            
                    
            
 
plt.subplot(1,2,1),plt.imshow(original),plt.title('Original')
plt.subplot(1,2,2),plt.imshow(dialationSample),plt.title('Sorted Around Light Sources')
cv2.imwrite( "Night_Rider.jpg", cv2.cvtColor(dialationSample, cv2.COLOR_RGB2BGR));

plt.show()

 
