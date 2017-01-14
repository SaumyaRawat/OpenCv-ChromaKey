import cv2
import numpy as np
import sys
import glob
import os

if len(sys.argv)<2:
	print('USAGE: ./images_to_video <fps>')
	sys.exit(0)

fps = float(sys.argv[1])
DIR = 'image_output'
no_of_images = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
files = sorted(glob.glob(DIR + '/*.jpg' ), key=lambda name: int(name[13:-4]))

img = cv2.imread(files[0],0)
height, width = img.shape[:2]

image_stack = np.empty((height, width, nIMAGES))
output_file = 'video_output' + '/' + 'video.mp4'
write_video = cv2.VideoWriter(filename=output_file, fourcc=cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps=fps, frameSize=(width, height)) # frame size is 220 x 500

for i in np.arange(0, no_of_images):
    print('Working on: ' + files[i])
    image = cv2.imread(files[i])
    crop_image = image[0:height, 0:width]
    write_video.write(crop_image)

write_video.release()