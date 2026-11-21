import cv2
import os
from PIL import Image

path=(r"C:\Users\henry\Documents\opencv\lesson 5\images")
os.chdir(path)
frames=[]
for i in os.listdir("."):
    if i.endswith((".avif",".jpg",".webp",".png",".jpeg")):
        frames.append(i)
totwidth=0
totheight=0
for i in frames: