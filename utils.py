import cv2
import numpy as np


def nothing(a):
   pass


def canny(img):
	###Step1 apply canny
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	edged_image = cv2.Canny(gray, 75,150)
	return edged_image
    
    
	edge_detected_image = cv2.Canny(mask, 50,150)
	return edge_detected_image
	###Step1 apply canny


'''def warpImg(img,points,w,h):
	points = np.float32(points)
	pts2 = np,float32([0,0], [w,0], [0,h],[w,h])
	matrix = cv2.getPerspectiveTransform(points,pts2)
	imgWarp = cv2.warpPerspective(img,matrix,(w,h))
	return imgWarp


def initializeTrackbar(initTrackbarvals, wT=480, hT=240):
	cv2.namedWindow("Trackbars")
	cv2.resizeWindow("Trackbars", 360,240)
	cv2.createTrackbar("Width top","Trackbars", initTrackbarvals[0], wT//2, nothing)
	cv2.createTrackbar("Height top","Trackbars", initTrackbarvals[1], hT, nothing)
	cv2.createTrackbar("Width bottom","Trackbars", initTrackbarvals[0], wT//2, nothing)
	cv2.createTrackbar("Height top","Trackbars", initTrackbarvals[0],hT, nothing)


def valTrackbars(wT=480, hT=240):
	widthTop = cv2.getTrackbarPos("Width top", "Trackbars")
	heightTop = cv2.getTrackbarPos("Height top", "Trackbars")
	widthBottom = cv2.getTrackbarPos("Width Bottom", "Trackbars")
	heightbottom = cv2.getTrackbarPos("Height bottom", "Trackbars")
	pts3 = np.float32([ (widthTop,heightTop), (wT-widthTop, heightTop), (widthBottom, heightbottom), (wT-widthBottom, heightbottom)])
	return pts3'''



def warpImg(img, inv = False):
	points = np.float32([[550,510],[800,510],[350,660],[980,660]])
	pts2 = np.float32([[0,0],[810,0],[0,670],[990,660]])


	if inv:
		matrix = cv2.getPerspectiveTransform(pts2,points)
	else:
		matrix = cv2.getPerspectiveTransform(points,pts2)

	imgwarp = cv2.warpPerspective(img,matrix,(990,650))
	return imgwarp



def getHistogram(img, display = False, minPer = 0.1,region = 1):
	if region==1:
		histvalue = np.sum(img,axis=0)   #sum all pixels in height
	else:
		histvalue = np.sum(img[img.shape[0]//region:,:], axis=0)

	
	maxvalue = np.max(histvalue) #check max value in np.sum
	minvalue = 0.1*maxvalue #min value to qualify as a path, in this case 10% of max, anything below is noise
	
	indexarray = np.where(histvalue >= minvalue) #find index of values which are >= minvalue
	basepoint = int(np.average(indexarray))

	if display:
		imgHist = np.zeros((img.shape[0],img.shape[1],3),np.uint8)

		for x,intensity in enumerate(histvalue):
			cv2.line(imgHist, (x,img.shape[0]),(x,img.shape[0]-intensity//255//region),(255,0,255),1)
			cv2.circle(imgHist,(basepoint,img.shape[0]),20,(0,255,255),cv2.FILLED)
		return basepoint, imgHist
	return basepoint





def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


	










