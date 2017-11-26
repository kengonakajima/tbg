import cv2
import numpy as np

img=cv2.imread("images/IMG_1519.jpg")
print("shape:",img.shape)
height, width, channels = img.shape[:3]
size=(640,480)
img=cv2.resize(img,size)

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
px=hsv[179,149]
print("hsv:",px)
cv2.imshow("hoge",hsv)
k=cv2.waitKey(0)

#	cvInRangeS(hsv, cvScalar(0.11*256, 0.60*256, 0.20*256, 0),
#	                cvScalar(0.14*256, 1.00*256, 1.00*256, 0), mask);

# 黄色いボールについてはこれでかなりいける
#l= (0.11*256, 0.60*256, 0.20*256)
#u=(0.14*256, 1.00*256, 1.00*256)

l= (0.11*256, 0.40*256, 0.20*256)
u=(0.16*256, 1.00*256, 1.00*256) # 0.16がいいかなぁ

        
#l = (0.11*25640, 10, 5)
#u = (90, 255, 255)
mask=cv2.inRange(hsv,l,u)
mask=cv2.erode(mask,None,iterations=2)
#mask=cv2.dilate(mask,None,iterations=1)
cv2.imshow("hoge",mask)
k=cv2.waitKey(0)

cv2.imwrite("mask.jpg",mask)

cv2.destroyAllWindows()
