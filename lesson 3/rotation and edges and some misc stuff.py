import cv2

planeimg=cv2.imread(r"C:\Users\henry\Documents\opencv\lesson 3\t-50-11.webp")
rows,columns=planeimg.shape[0:2]
print(rows,columns)
rotationmatrix=cv2.getRotationMatrix2D((rows/2,columns/2),20,1)
rotatedplaneimg=cv2.warpAffine(planeimg,rotationmatrix,(rows,columns))
#cv2.imshow("rotated",rotatedplaneimg)
#cv2.waitKey(0)

edges=cv2.Canny(planeimg,100,155)
#cv2.imshow("edges",edges)
#cv2.waitKey(0)

planeimgdraw=cv2.line(planeimg,(100,100),(200,200),(0,0,0),10)
planeimgdraw=cv2.line(planeimgdraw,(200,200),(100,200),(0,0,0),10)
planeimgdraw=cv2.line(planeimgdraw,(100,200),(100,100),(0,0,0),10)
planeimgdraw=cv2.rectangle(planeimgdraw,(95,205),(205,315),(255,0,0),-10)
planeimgdraw=cv2.circle(planeimgdraw,(150,260),50,(0,0,255),-10)
planeimgdraw=cv2.putText(planeimgdraw,"Plane",(540,358),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,0),5)
cv2.imshow("line",planeimgdraw)
cv2.waitKey(0)