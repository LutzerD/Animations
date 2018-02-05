import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('fence.jpg')
rows,cols,ch = img.shape

print(rows)
print(cols)
print(ch)

#pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])

#pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

pts2 = np.float32([[0,0],[600,600],[0,600],[600,0]])
pts1 = np.float32([[0,350],[0,550],[600,330],[600,400]])


M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
