import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from scipy.stats import itemfreq
import requests
import os

path = 'results'
pixel = 50


def get_frequent_color(path)
    img = cv2.imread(path)
    img = cv2.resize(img,None,fx=.05, fy=.1, interpolation = cv2.INTER_CUBIC)

    average_color = [img[:, :, i].mean() for i in range(img.shape[-1])]

    arr = np.float32(img)
    pixels = arr.reshape((-1, 3))

    n_colors = 3
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    _, labels, centroids = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)

    palette = np.uint8(centroids)
    quantized = palette[labels.flatten()]
    quantized = quantized.reshape(img.shape)

    return palette[np.argmax(itemfreq(labels)[:, -1])]

#main_color = img.copy()
#print(main_color.shape)
#print(dominant_color)
#main_color[:,:,0] = dominant_color[0]
#main_color[:,:,1] = dominant_color[1]
#main_color[:,:,2] = dominant_color[2]

##so i need to resize main image to certain thing, change each one of those pixels into a new image
##like take the top left n pixels, or expand it if it's


for filename in os.listdir('results'):
    if filename.endswith(".jpg") or filename.endswith(".png"):
            try:
                matches(get_frequent_color('results/'+filename)
            except:
                print('rekt by non-image' + filename)
        continue
    else:
        continue


#Now go through all the relevant results and crash this party

plt.subplot(1,2,1),plt.imshow(img),plt.title('Original')
plt.subplot(1,2,2),plt.imshow(main_color),plt.title('Main Color(s)')

plt.show()
