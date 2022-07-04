import cv2
import mediapipe as mp
import time
import Hand_Tracking_Module as htm


cap = cv2.VideoCapture(0) # 1 ?
pTime = 0
cTime = 0
detector = htm.HandDetector()
while 1:
	success, img = cap.read()
	img = detector.find_hands(img)
	lm_list = detector.find_position(img)
	if lm_list:
		print(lm_list[4])

	cTime = time.time()
	fps = 1/(cTime - pTime)
	pTime = cTime

	cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
	cv2.imshow("Image", img)
	cv2.waitKey(1)
