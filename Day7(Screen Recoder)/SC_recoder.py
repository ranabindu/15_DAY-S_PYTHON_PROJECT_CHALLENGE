import cv2            #OpenCV library for computer vision tasks, used here for creating and writing video files
import pyautogui      # A library to control the mouse, keyboard, and take screenshots
from win32api import GetSystemMetrics    #Function to get the screen's width and height, i.e., the screen resolution
import numpy as np       #A library for numerical operations, used here to manipulate image data
import time           #A library to work with time-related tasks, such as measuring duration
width =  GetSystemMetrics(0)           # Retrieves the width of the screen in pixels
height =  GetSystemMetrics(1)       # Retrieves the height of the screen in pixels 
dim = (width, height)           #A tuple storing the screen dimensions, which will be used as the resolution for the video
f = cv2.VideoWriter_fourcc(*"mp4v")    #This function specifies the codec to be used for encoding the video. Here, "mp4v" is a codec suitable for MP4 files
output = cv2.VideoWriter("test.mp4",f, 30.0,dim)   # Creates a video writer object that: "test.mp4": Defines the filename for the output video/f: Uses the specified codec ("mp4v")/30.0: Sets the frame rate to 30 frames per second/dim: Uses the screen dimensions as the resolution for the video
now_start_time = time.time()        #Returns the current time in seconds since the epoch 
dur = 10                            #Sets the duration for the screen recording to 10 seconds
end_time = now_start_time  + dur    #Calculates the end time by adding the duration to the current time
while True:                     #This starts an infinite loop that will continue running until the specified duration has passed
  image = pyautogui.screenshot()   #Captures the current screen and stores the image in the image variable
  frame_1 = np.array(image)     #Converts the captured image into a numpy array, which is the format that OpenCV requires for further processing
  frame = cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)   #Converts the color format from BGR (which OpenCV uses by default) to RGB (which most image viewers use). This step ensures that the colors in the video are accurate
  output.write(frame)    #Adds the current frame (screenshot) to the video file, effectively recording the screen      
  c_time = time.time()   #Captures the current time
  if c_time>end_time:    #Checks if the current time has passed the end time. If it has, the loop breaks, stopping the recording process
    break                #stop while loop 
output.release()       #Releases the video writer object, finalizing and saving the video file
print("--- END---" )   #Outputs a message indicating that the screen recording has ended