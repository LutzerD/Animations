import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('liz.jpeg',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx1 = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely1 = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

sobely = cv2.Sobel(sobelx1,cv2.CV_64F,0,1,ksize=5)
sobelx = cv2.Sobel(sobely1,cv2.CV_64F,1,0,ksize=5)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
#plt.subplot(2,2,1),plt.imshow(img)
#plt.title('Original'), plt.xticks([]), plt.yticks([])
#plt.subplot(2,2,2),plt.imshow(laplacian)
#plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
#plt.subplot(2,2,3),plt.imshow(sobelx)
#plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
#plt.subplot(2,2,4),plt.imshow(sobely)
#plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()
