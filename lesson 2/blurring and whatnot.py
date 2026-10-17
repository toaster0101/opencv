import cv2
import numpy as np

plane=cv2.imread(r"C:\Users\henry\Documents\opencv\lesson 2\planeimg.jpg")
plane=cv2.resize(plane,(700,525))
display=cv2.imread(r"C:\Users\henry\Documents\opencv\lesson 2\displayimg.jpg")
subtractedimg=cv2.subtract(plane,display)
cv2.imshow("subtracted",subtractedimg)
cv2.waitKey(0)

kernel=np.ones((3,3),np.uint8)
erodedimg=cv2.erode(plane,kernel)
cv2.imshow("eroded",erodedimg)
cv2.waitKey(0)

blurredgausimg=cv2.GaussianBlur(plane,(7,7),0)
cv2.imshow("blurred1",blurredgausimg)
cv2.waitKey(0)

blurredmedianimg=cv2.medianBlur(plane,5)
cv2.imshow("blurred2",blurredmedianimg)
cv2.waitKey(0)

blurredbylatimg=cv2.bilateralFilter(plane,7,75,75)
cv2.imshow("blurred3",blurredbylatimg)
cv2.waitKey(0)
