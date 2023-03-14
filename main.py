import cv2

img = cv2.imread("picture.jpg")

cv2.imshow("Picture", img)
cv2.waitKey(0)