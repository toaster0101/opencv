import cv2
import os

path=r"C:\Users\henry\Documents\opencv\lesson 1\hw images"

landscape=cv2.imread(r"C:\Users\henry\Documents\opencv\lesson 1\landscape.jpg",1)
cv2.imshow("landscape",landscape)
cv2.waitKey(0)

landscape_grey=cv2.cvtColor(landscape,cv2.COLOR_BGR2GRAY)
cv2.imshow("landscape_grey",landscape_grey)
cv2.waitKey(0)

landscape_HSV=cv2.cvtColor(landscape,cv2.COLOR_BGR2HSV)
cv2.imshow("landscape_HSV",landscape_HSV)
cv2.waitKey(0)

os.chdir(path)
cv2.imwrite("landscape.jpg",landscape)

os.chdir(path)
cv2.imwrite("landscape_grey.jpg",landscape_grey)

os.chdir(path)
cv2.imwrite("landscape_HSV.jpg",landscape_HSV)