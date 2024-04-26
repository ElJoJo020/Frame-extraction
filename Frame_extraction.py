import cv2 
import numpy as np
  
# Function to extract frames 
def FrameCapture(path): 
  
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
  
        # Saves the frames with frame-count 
        cv2.imwrite("D:/CICY/DJI35_17/dji_testframe%d.tiff" % count, image) 
  
        count += 1

    cv2.cap_pv
  
# Driver Code 
if __name__ == '__main__': 
  
    # Calling the function 
    FrameCapture("D:/CICY/DJI_0135.mp4") 
    
