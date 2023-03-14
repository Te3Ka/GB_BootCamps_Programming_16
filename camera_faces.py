import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

camera = cv2.VideoCapture(0)

while True:
	success, frame = camera.read()
	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascades.detectMultiScale(frame_gray)

	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 4)
	
	cv2.imshow("Web-Camera-Faces", frame)

	if cv2.waitKey(1) & 0xff == ord('q'):
		break
