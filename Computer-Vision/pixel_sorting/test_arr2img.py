import numpy as np
import cv2
a = np.array([[i for i in range(0,255)] for j in range(0,255)],dtype=np.uint8)
b = np.array([[255 for i in range(0,255)]for j in range(0,255)],dtype=np.uint8)
c = b.copy()
pic = np.dstack((a,b,c))
cv2.imwrite( "test.jpg", cv2.cvtColor(pic, cv2.COLOR_RGB2BGR));
