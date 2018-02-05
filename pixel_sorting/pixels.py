import numpy as np
import cv2
from matplotlib import pyplot as plt

#img = cv2.imread("hotel.jpg") #900,1440,3
#img = cv2.imread("gradient.png") #256,256,3
#img = cv2.imread("Lenna.png") #1080,1920
img = cv2.imread("tron.png")

print(img.shape)
x,y,z = img.shape
img = cv2.resize(img,(round(y/10)*10, round(x/10)*10),interpolation = cv2.INTER_CUBIC)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
original_shape = np.array(hsv.shape).astype(int)
print(original_shape)

n = 0

while(1):
    #reshaped = np.reshape(hsv,(90,180,-1,3))
    #reshaped = np.reshape(hsv,(108,192,-1,3))
    reshaped = np.reshape(hsv,(int(original_shape[1]/10),int(original_shape[0]/10),-1,3))
    reshaped_sorted = np.sort(reshaped,axis = n)
    reshaped_sorted = np.reshape(reshaped_sorted,hsv.shape)
    reshaped_sorted  = cv2.cvtColor(reshaped_sorted, cv2.COLOR_HSV2RGB)

#cool effect
    #reshaped2 = np.reshape(hsv,(90,100,-1,3))
    reshaped2 = np.reshape(hsv,(int(original_shape[1]/5),int(original_shape[0]/10),-1,3))
    reshaped_sorted2 = np.sort(reshaped2,axis = 2)
    reshaped_sorted2 = np.reshape(reshaped_sorted2,hsv.shape)
    reshaped_sorted2  = cv2.cvtColor(reshaped_sorted2, cv2.COLOR_HSV2RGB)
           
    #reshaped3 = np.reshape(hsv,(90,144,-1,3))
    reshaped3 = np.reshape(hsv,(int(original_shape[1]/5),int(original_shape[0]/20),-1,3))
    reshaped_sorted3 = np.sort(reshaped3,axis = n)
    reshaped_sorted3 = np.reshape(reshaped_sorted3,hsv.shape)
    reshaped_sorted3  = cv2.cvtColor(reshaped_sorted3, cv2.COLOR_HSV2RGB)


#    reshaped4 = np.reshape(hsv,(int(original_shape[1]/20),int(original_shape[0]/5),-1,3))
#    reshaped_sorted4 = np.sort(reshaped4,axis =n)#
#    reshaped_sorted4 = np.reshape(reshaped_sorted4,hsv.shape)
#    reshaped_sorted4  = cv2.cvtColor(reshaped_sorted4, cv2.COLOR_HSV2RGB)

#cool effect
    reshaped4 = np.reshape(hsv,(int(original_shape[0]/5),-1,int(original_shape[1]/20),3))
    reshaped_sorted4 = np.sort(reshaped4,axis = 2) #flip around axis i fugkec up n didnt note it
    reshaped_sorted4 = np.reshape(reshaped_sorted4,hsv.shape)
    reshaped_sorted4  = cv2.cvtColor(reshaped_sorted4, cv2.COLOR_HSV2RGB)


    plt.subplot(3,2,1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ),plt.title('Original')
    plt.subplot(3,2,2),plt.imshow(np.sort(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    , axis=1)),plt.title('Sorted by Row')
    plt.subplot(3,2,3),plt.imshow(reshaped_sorted),plt.title('x/10, y/10\nAxis=2')
    plt.subplot(3,2,4),plt.imshow(reshaped_sorted2),plt.title('x/5, y/10\nAxis=2')
    plt.subplot(3,2,5),plt.imshow(reshaped_sorted3),plt.title('x/10, y/5\nAxis=0')
    plt.subplot(3,2,6),plt.imshow(reshaped_sorted4),plt.title('x/5, y/5\nAxis=0')
    plt.show()

    n = n+1
