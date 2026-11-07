import cv2

traffic=cv2.imread(r"C:\Users\henry\Documents\opencv\lesson 3\images.png")
traffic=cv2.rectangle(traffic,(120,84),(134,114),(0,0,0),-1)
traffic=cv2.circle(traffic,(127,99),5,(0,255,255),-1)
traffic=cv2.circle(traffic,(127,109),5,(0,0,255),-1)
traffic=cv2.circle(traffic,(127,89),5,(0,255,0),-1)
traffic=cv2.rectangle(traffic,(110,74),(144,124),(0,0,0),2)
traffic=cv2.rectangle(traffic,(100,34),(184,70),(0,255,0),-1)
traffic=cv2.rectangle(traffic,(99,33),(185,71),(0,0,0),1)
traffic=cv2.putText(traffic,"light",(110,64),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)
cv2.imshow("traffic",traffic)
cv2.waitKey(0)