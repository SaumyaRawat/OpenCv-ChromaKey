import cv2
print(cv2.__version__)
vidcap = cv2.VideoCapture(0)
success,image = vidcap.read()
count = 0
success = True

while success:
	success,image = vidcap.read()
	cv2.imwrite("image_output/%d.jpg" % count, image)	 # save frame as JPEG file
	print('Writing Frame: ' + str(count) + ' Press q to exit.')
	count += 1
	cv2.imshow('frame',image)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


# Release everything if job is finished
vidcap.release()
cv2.destroyAllWindows()
