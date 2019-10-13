from mpl_toolkits import mplot3d
import cv2
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing


src="./mkbhd.png"
detail = 60

img = cv2.imread(src)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.axis('off')
ax.view_init(50, 90)
ax.set_facecolor('xkcd:dark grey')

for y in range(0, len(img)):
    if y%detail == 0:

        yArray = [y]*len(img)
        xArray = range(0, len(yArray))
        zArray = gray[y][0:len(yArray)] 

        ax.plot3D(xArray,yArray, zArray, c="grey")

        print(y)    
        
plt.show()