# Just testing things out to get the video/ img to show up in python

import numpy as np
import cv2

cap = cv2.VideoCapture('C:\\Users\\joshu\\Dropbox\\My PC (JoshuaZob-Center)\\Desktop\\HackAthon\\drop.avi')
while(cap.isOpened()):
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('frame',gray)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

