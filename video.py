import cv2

camera = cv2.VideoCapture(0)

while True:
	success, frame = camera.read()
	cv2.imshow("Web-Camera", frame)
	
	if cv2.waitKey(1) & 0xff == ord('q'):
		break
