import os

from threading import Thread
from datetime import datetime

from recorder import Recorder
from screenRecorder import ScreenRecorder

def main():
    recorder = Recorder()
    scr = ScreenRecorder()

    video = Thread(target = scr.startRecording)
    video.start()
    recorder.record(scr)
    video.join()

    filename = f"output-{datetime.today().strftime('%Y-%m-%d-%H%M%S')}"
    os.system(f"ssw_program\\bin\\ffmpeg.exe -i output.avi -i output.wav -map 0:v -map 1:a -c:v copy -shortest {filename}.mp4")
    while not os.path.exists(f"{filename}.mp4"):
        pass
    os.rename(f"{filename}.mp4", f"ssw_program\\sound_spectrum\\{filename}.mp4")
    os.remove("output.wav")
    os.remove("output.avi")

if __name__ == "__main__":
    main()