# Just testing things out to get the video/ img to show up in python

import numpy as np
import cv2

cap = cv2.VideoCapture('wav_files\Blue.wav')
while(cap.isOpened()):
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('frame',gray)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

