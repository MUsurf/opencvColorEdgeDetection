import cv2 as cv

img = cv.imread('testimage.png')

cv.imshow('test', img)

cv.waitKey(0)
