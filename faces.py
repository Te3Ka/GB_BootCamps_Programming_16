import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img = cv2.imread("face.jpg")
img = cv2.resize(img, (480, 640))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascades.detectMultiScale(img_gray)

for (x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

cv2.imshow("Faces", img)
cv2.waitKey(0)