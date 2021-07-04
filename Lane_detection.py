import cv2
import numpy as np
import utils
import matplotlib.pyplot as plt



curveList = []

def getLaneCurve(img):

	#Step 1 canny the image
	image_cannied = utils.canny(img)
	#cv2.imshow("canny", image_cannied)
	#step 2 warping (bird's eye view)
		

	imgWarp = utils.warpImg(image_cannied)
	#print(imgWarp)
	cv2.imshow('imgWarp',imgWarp)
	#Step3 histogram
	middlePoint,imgHist = utils.getHistogram(imgWarp, display= True, minPer = 0.5,region = 4)
	curveAveragePoint,imgHist = utils.getHistogram(imgWarp, display= True, minPer = 0.9)
	curveRaw = curveAveragePoint-middlePoint
	print(curveAveragePoint-middlePoint)



	#print(basepoint)
	#cv2.imshow('histogram', imgHist)
	


	### STEP 4 to keep curveRaw smooth and not jump between values
	curveList.append(curveRaw)
	if len(curveList)> 10:
		curveList.pop(0)
	curve = int(sum(curveList)/len(curveList))
	a = cv2.circle(frame,(curve,img.shape[0]),20,(0,255,255),cv2.FILLED)
	cv2.imshow("test",a)
	return None


	

	
	
		
		





#b = cv2.circle(frame, curve, 5,(0,255,255) )


cap = cv2.VideoCapture('check1.mp4')
while True:
	ret, frame = cap.read()
	getLaneCurve(frame)
	
		
			
	key = cv2.waitKey(4)
	if key == 27:
		break


	
		

cap.release()
cv2.destroyAllWindows()
			
