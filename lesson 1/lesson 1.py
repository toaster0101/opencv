import cv2
import os

path=r"C:\Users\henry\Documents\opencv\lesson 1\images"

saveimage=cv2.imread(r"C:\Users\henry\Documents\opencv\lesson 1\httpsstatics3.seeedstudio.comimagesproductlcd2016x220characters.jpg")
cv2.imshow("Image",saveimage)
cv2.waitKey(0)

#saveimage2=cv2.imread(r"C:\Users\henry\Documents\opencv\lesson 1\httpsstatics3.seeedstudio.comimagesproductlcd2016x220characters.jpg",0)
#cv2.imshow("Image2",saveimage2)
#cv2.waitKey(0)

#os.chdir(path)
#cv2.imwrite("electronic.jpg",saveimage)

#b,g,r=(cv2.split(saveimage))
#cv2.imshow("BLUE",b)
#cv2.waitKey(0)
#cv2.imshow("GREEN",g)
#cv2.waitKey(0)
#cv2.imshow("RED",r)
#cv2.waitKey(0)

#greyimg=cv2.cvtColor(saveimage,cv2.COLOR_BGR2GRAY)
#cv2.imshow("GREY",greyimg)
#cv2.waitKey(0)

#hsvimg=cv2.cvtColor(saveimage,cv2.COLOR_BGR2HSV)
#cv2.imshow("HSV",hsvimg)
#cv2.waitKey(0)

#RGBimg=cv2.cvtColor(saveimage,cv2.COLOR_BGR2RGB)
#cv2.imshow("RGB",RGBimg)
#cv2.waitKey(0)

#os.chdir(path)
#cv2.imwrite("RGB.jpg",RGBimg)

#saveimagesized=cv2.resize(saveimage,(597,335))
#cv2.imshow("SIZED",saveimagesized)
#cv2.waitKey(0)

#planeImg=cv2.imread(r"C:\Users\henry\Documents\opencv\lesson 1\images.jpg")
#cv2.imshow("PLANE",planeImg)
#cv2.waitKey(0)

#merged=cv2.addWeighted(saveimagesized,0.5,planeImg,0.5,-50)
#cv2.imshow("MERGED",merged)
#cv2.waitKey(0)

print(saveimage)