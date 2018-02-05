import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("hotel.jpg")
#img = cv2.imread("gradient.png")
img = np.array(img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
original_shape = hsv.shape

reshaped = np.reshape(hsv,(90,180,-1,3))
reshaped_sorted = np.sort(reshaped,axis = 2)
reshaped_sorted = np.reshape(reshaped_sorted,hsv.shape)
reshaped_sorted  = cv2.cvtColor(reshaped_sorted, cv2.COLOR_HSV2BGR)


reshaped2 = np.reshape(hsv,(180,360,-1,3))
reshaped_sorted2 = np.sort(reshaped2,axis = 2)
reshaped_sorted2 = np.reshape(reshaped_sorted2,hsv.shape)
reshaped_sorted2  = cv2.cvtColor(reshaped_sorted2, cv2.COLOR_HSV2BGR)
       
reshaped3 = np.reshape(hsv,(100,180,-1,3))
reshaped_sorted3 = np.sort(reshaped3,axis = 2)
reshaped_sorted3 = np.reshape(reshaped_sorted3,hsv.shape)
reshaped_sorted3  = cv2.cvtColor(reshaped_sorted3, cv2.COLOR_HSV2BGR)


reshaped4 = np.reshape(hsv,(360,360,-1,3))
reshaped_sorted4 = np.sort(reshaped4,axis = 2)
reshaped_sorted4 = np.reshape(reshaped_sorted4,hsv.shape)
reshaped_sorted4  = cv2.cvtColor(reshaped_sorted4, cv2.COLOR_HSV2BGR)

print(reshaped_sorted.shape)

plt.subplot(3,2,1),plt.imshow(img),plt.title('Original')
plt.subplot(3,2,2),plt.imshow(np.sort(img, axis=1)),plt.title('Sorted by Row')
plt.subplot(3,2,3),plt.imshow(reshaped_sorted),plt.title('Sorted in groups of 8x10\nAxis=2')
plt.subplot(3,2,4),plt.imshow(reshaped_sorted2),plt.title('Sorted in groups of 16x20\nAxis=2')
plt.subplot(3,2,5),plt.imshow(reshaped_sorted3),plt.title('Sorted in groups of 8x10\nAxis=0')
plt.subplot(3,2,6),plt.imshow(reshaped_sorted4),plt.title('Sorted in groups of 16x20\nAxis=0')
plt.show()
