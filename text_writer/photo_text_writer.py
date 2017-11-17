#!/usr/bin/env python3.6
import cv2 as cv



print("image reading")
img = cv.imread('sample.jpg')
#cv.putText(img, 'HELLO', (0,50), cv.FONT_HERSHEY_PLAIN, 4, (0,0,0), 5, cv.LINE_AA)
cv.putText(img, 'HELLO', (0,50),cv.FONT_HERSHEY_TRIPLEX, 2, (100,200,200), 5, cv.LINE_AA)
cv.putText(img, 'WORLD!', (150,200),cv.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (100,255,200), 5, cv.LINE_AA)
cv.imwrite('sample6.jpg', img)
print("DONE !")