#Importing all necessary libraries
import cv2
import os

# Open a video file or image file sequence or a capturing device or an IP video stream for video capturing.
cam = cv2.VideoCapture("/Users/rajeshtiwari/Desktop/Video53-AI.mp4")

# Creating a folder to store all extracted frames
try:
	# creating a folder named Frames
	if not os.path.exists('video_frames23'):
		os.makedirs('video_frames23')
# if not created then raise error
except OSError:
	print ('Error: Creating directory of video_frames23')

# Extracting frames and saving it 
currentframe = 1# keep a count of created frames

while cam.isOpened():

  # ret is a boolean variable that returns true if the frame is available
  # frame is an image array vector captured based on the default frames per second defined explicitly or implicitly

	ret,frame = cam.read()#method returns a tuple, where the first element is a boolean and the next element is the actual video frame
 
	if ret:
		# continue creating frames
		name = './video_frames23/frame' + str(currentframe) + '.png'
		print ('Creating...' + name)

		# writing the extracted frames
		cv2.imwrite(name, frame)

		# increasing counter to keep a count of created frames
		currentframe += 1
	else:
		break

print('frame_rate:', (currentframe/24),'fps')#time duration of 112 seconds  

# release the resources that we have initialized for our code
cam.release()
cv2.destroyAllWindows()