#!/usr/bin/env python
# coding: utf-8
import numpy as np
import cv2
from imutils.object_detection import non_max_suppression
import pytesseract
from matplotlib import pyplot as plt
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
def open_main(y):
	x = y
	args = {"image": x, "east": "east_text_detection.pb", "min_confidence": 0.5, "width": 320, "height": 320}
	args['image'] = x
	image = cv2.imread(args['image'])
	image_ex=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
	text_return=(pytesseract.image_to_string(image_ex))
	print(''.join(text_return),end='')
	boxes=pytesseract.image_to_data(image_ex)
	for x,b in enumerate(boxes.splitlines()):
		if(x!=0):
			b=b.split()
			if(len(b)==12):
				x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
				cv2.rectangle(image_ex,(x,y),(w+x,h+y),(0,0,255),3)
				cv2.putText(image_ex,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
	orig = image.copy()
	(origH, origW) = image.shape[:2]
	(newW, newH) = (args["width"], args["height"])
	rW = origW / float(newW)
	rH = origH / float(newH)
	image = cv2.resize(image, (newW, newH))
	(H, W) = image.shape[:2]
	blob = cv2.dnn.blobFromImage(image, 1.0, (W, H), (123.68, 116.78, 103.94), swapRB=True, crop=False)
	net = cv2.dnn.readNet(args["east"])
	layerNames = ["feature_fusion/Conv_7/Sigmoid", "feature_fusion/concat_3"]
	net.setInput(blob)
	(scores, geometry) = net.forward(layerNames)

	def predictions(prob_score, geo):
		(numR, numC) = prob_score.shape[2:4]
		boxes = []
		confidence_val = []
		for y in range(0, numR):
			scoresData = prob_score[0, 0, y]
			x0 = geo[0, 0, y]
			x1 = geo[0, 1, y]
			x2 = geo[0, 2, y]
			x3 = geo[0, 3, y]
			anglesData = geo[0, 4, y]
			for i in range(0, numC):
				if scoresData[i] < args["min_confidence"]:
					continue
				(offX, offY) = (i * 4.0, y * 4.0)
				angle = anglesData[i]
				cos = np.cos(angle)
				sin = np.sin(angle)
				h = x0[i] + x2[i]
				w = x1[i] + x3[i]
				endX = int(offX + (cos * x1[i]) + (sin * x2[i]))
				endY = int(offY - (sin * x1[i]) + (cos * x2[i]))
				startX = int(endX - w)
				startY = int(endY - h)
				boxes.append((startX, startY, endX, endY))
				confidence_val.append(scoresData[i])
		return (boxes, confidence_val)

	(boxes, confidence_val) = predictions(scores, geometry)
	boxes = non_max_suppression(np.array(boxes), probs=confidence_val)
	results = []
	shobhit = []
	# loop over the bounding boxes to find the coordinate of bounding boxes
	for (startX, startY, endX, endY) in boxes:
		startX = int(startX * rW)
		startY = int(startY * rH)
		endX = int(endX * rW)
		endY = int(endY * rH)
		r = orig[startY:endY, startX:endX]
		configuration = ("-l eng --oem 1 --psm 8")
		text = pytesseract.image_to_string(r, config=configuration)
		#shubhiankit.append(text)
		# text=" "
		results.append(((startX, startY, endX, endY), text))
	orig_image = orig.copy()

	for ((start_X, start_Y, end_X, end_Y), text) in results:
		#print("{}\n".format(text))
		shobhit.append(text.replace('\n\x0c',''))
		text = "".join([x if ord(x) < 128 else "" for x in text]).strip()
		cv2.rectangle(orig_image, (start_X, start_Y), (end_X, end_Y), (0, 0, 255), 2)
		cv2.putText(orig_image, text, (start_X, start_Y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
	text=" ".join(shobhit)
	return text_return,image_ex
def show_output(orig_image):
	plt.imshow(orig_image)
	plt.title('Output')
	plt.show()