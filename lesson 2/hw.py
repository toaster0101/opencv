import cv2
import numpy as np

planeimg=cv2.imread(r"C:\Users\henry\Documents\opencv\lesson 2\t-50-11.webp")
cv2.imshow("normal",planeimg)
cv2.waitKey(0)

kernel=np.ones((3,3),np.uint8)
eroded1=cv2.erode(planeimg,kernel)
cv2.imshow("eroded",eroded1)
cv2.waitKey(0)

kernel=np.ones((5,5),np.uint8)
eroded2=cv2.erode(planeimg,kernel)
cv2.imshow("eroded",eroded2)
cv2.waitKey(0)

kernel=np.ones((7,7),np.uint8)
eroded3=cv2.erode(planeimg,kernel)
cv2.imshow("eroded",eroded3)
cv2.waitKey(0)

planeimgresized=cv2.resize(planeimg,(540,357))

planeborder=cv2.copyMakeBorder(planeimgresized,75,75,75,75,cv2.BORDER_CONSTANT,value=(0,0,0))
cv2.imshow("border",planeborder)
cv2.waitKey(0)