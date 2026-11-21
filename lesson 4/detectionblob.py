import cv2
import numpy as np

circles=cv2.imread(r"C:\Users\henry\Documents\opencv\lesson 4\coins.jpg")#
cv2.imshow("original",circles)
cv2.waitKey(0)

settings=cv2.SimpleBlobDetector_Params()

settings.filterByArea=True
settings.minArea=1000
settings.maxArea=100000

settings.filterByCircularity=True
settings.minCircularity=0.1

settings.filterByConvexity=True
settings.minConvexity=0.1

settings.filterByInertia=True
settings.minInertiaRatio=0.1

detecterOfCircles=cv2.SimpleBlobDetector_create(settings)
keyPoints=detecterOfCircles.detect(circles)
circlesint=len(keyPoints)
circles=cv2.drawKeypoints(circles,keyPoints,circles,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.putText(circles,str(circlesint),(3,27),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),5)
cv2.imshow("detected",circles)
cv2.waitKey(0)