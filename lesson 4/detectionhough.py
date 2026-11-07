import cv2
import numpy as np

circles=cv2.imread(r"C:\Users\henry\Documents\opencv\lesson 4\circles3.webp")
#circles=cv2.resize(circles,(579,772))
cv2.imshow("original",circles)
cv2.waitKey(0)
circlesGrey=cv2.cvtColor(circles,cv2.COLOR_BGR2GRAY)
circlesGreyBlur=cv2.blur(circlesGrey,(3,3))
#cv2.imshow("processed",circlesGreyBlur)
#cv2.waitKey(0)

detectedCircles=cv2.HoughCircles(circlesGreyBlur,cv2.HOUGH_GRADIENT,1,100,param1=45,param2=25,minRadius=10,maxRadius=50)
detectedCircles=np.uint16(np.round(detectedCircles))

for i in detectedCircles[0,:]:
    circles=cv2.circle(circles,(i[0],i[1]),i[2],(0,0,255),3)
    cv2.imshow("detected",circles)
    cv2.waitKey(1000)