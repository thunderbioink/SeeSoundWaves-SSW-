

from threading import Thread
import multiprocessing
import time

from recorder import Recorder
from screenRecorder import ScreenRecorder

def main():
    recorder = Recorder()
    scr = ScreenRecorder()

    #audio = multiprocessing.Process(target = recorder.record)
    video = Thread(target = scr.startRecording)
    #audio.start()
    video.start()
    # time.sleep(10)
    #audio.join()
    recorder.record()
    scr.record = False
    video.join()

if __name__ == "__main__":
    main()