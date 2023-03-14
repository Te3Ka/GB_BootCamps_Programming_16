import cv2

img = cv2.imread("picture.jpg")
print(img.shape)
img = cv2.resize(img, (400, 400))
print(img.shape)
