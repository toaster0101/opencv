import cv2
import numpy as np

circles=cv2.imread(r"C:\Users\henry\Documents\opencv\lesson 4\circles3.webp")#
cv2.imshow("original",circles)
cv2.waitKey(0)

settings=cv2.SimpleBlobDetector_Params()
settings.filterByArea=True
settings.minArea=100
settings.maxArea=10000
settings.filterByCircularity=True
settings.minCircularity=0.25