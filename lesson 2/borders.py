import cv2

landscape=cv2.imread(r"C:\Users\henry\Documents\opencv\lesson 2\landscape.jpg")
landscapeColourSolid=cv2.copyMakeBorder(landscape,50,50,50,50,cv2.BORDER_CONSTANT,value=(0,0,0))
cv2.imshow("landscapeBorder",landscapeColourSolid)
cv2.waitKey(0)

landscapeReflect=cv2.copyMakeBorder(landscape,50,50,50,50,cv2.BORDER_REFLECT)
cv2.imshow("landscapeBorder",landscapeReflect)
cv2.waitKey(0)