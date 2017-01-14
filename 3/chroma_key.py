import cv2
import numpy as np
print(cv2.__version__)

# Webcam Capture
#bgcap = cv2.VideoCapture(0)
# Existing Video Capture
bgcap = cv2.VideoCapture('bg.mp4')
fgcap = cv2.VideoCapture('fg.mp4')

success,bg_frame = bgcap.read()
ret,fg_frame = fgcap.read()

count = 0
success = True

while success:
	success,bg_frame = bgcap.read()
	ret,fg_frame = fgcap.read()

	output = np.where(bg_frame == (100,255,50), fg_frame, bg_frame)

	print('Press q to exit')

	cv2.imshow('frame',output)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


# Release everything if job is finished
bgcap.release()
fgcap.release()
cv2.destroyAllWindows()
