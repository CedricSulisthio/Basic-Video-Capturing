import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()  # Ret = 1 if the video is captured; frame is the image
    
    # Our operations on the frame come here    
    img = cv2.flip(frame, 1)   # Flip left-right  
    # img = cv2.flip(img, 0)   # Flip up-down
    
    # Display the resulting image
    cv2.imshow('Video Capture',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press q to quit
        break
        
# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()