import cv2
print(cv2.__version__)
vidcap = cv2.VideoCapture('video.mp4')
success,image = vidcap.read()
count = 0
success = True

while success:
  success,image = vidcap.read()
  cv2.imwrite("image_output/%d.jpg" % count, image)     # save frame as JPEG file
  print('Writing Frame: ' + count)
  count += 1