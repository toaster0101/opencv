import cv2
import numpy as np

coins=cv2.imread(r"C:\Users\henry\Documents\opencv\lesson 4\coins.jpg")
#circles=cv2.resize(circles,(579,772))
cv2.imshow("original",coins)
cv2.waitKey(0)
coinsGrey=cv2.cvtColor(coins,cv2.COLOR_BGR2GRAY)
coinsGreyBlur=cv2.blur(coinsGrey,(3,3))

detectedCircles=cv2.HoughCircles(coinsGreyBlur,cv2.HOUGH_GRADIENT,1,100,param1=45,param2=25,minRadius=10,maxRadius=40)
#param1 = higher value is fewer edges, lower is higher, controls edge detection using canny edge detector
#param2 = how close it has to be to a circle to be decected in %
detectedCircles=np.uint16(np.round(detectedCircles))

for i in detectedCircles[0,:]:
    coins=cv2.circle(coins,(i[0],i[1]),i[2],(0,255,0),3)
    cv2.imshow("detected",coins)
    cv2.waitKey(1000)