import cv2
import numpy as np
import pyautogui

class ScreenRecorder:

    def __init__(self, fileName="output.avi"):
        # display screen resolution, get it from your OS settings
        codec = cv2.VideoWriter_fourcc(*"XVID")
        self.scrRecorder = cv2.VideoWriter(fileName, codec, 20.0, (1920, 1080))
        self.record = True

    def startRecording(self):
        while self.record:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.scrRecorder.write(frame)
            #cv2.imshow("screenshot", frame)

    def stopRecording(self):
        self.record = False
        cv2.destroyAllWindows()
        self.scrRecorder.release()