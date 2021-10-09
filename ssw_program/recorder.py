import argparse
import queue
import sys

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd


from scipy.io.wavfile import write
import time
import cv2

class Recorder:

    def __init__(self):
        self.start_time = time.time()
        self.fs = 44100


    def check(self, text):
        try:
            return int(text)
        except ValueError:
            return text


    def audio_cb(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(indata[::self.args.downsample, self.mapping])


    def update_plot(self, frame):
        while True:
            try:
                data = self.q.get_nowait()
            except queue.Empty:
                break
            shift = len(data)
            self.plotdata = np.roll(self.plotdata, -shift, axis=0)
            self.plotdata[-shift:, :] = data
        for column, line in enumerate(self.lines):
            line.set_ydata(self.plotdata[:, column])
        return self.lines

    def record(self, scrdControl):
        self.start = time.time()
        print("Recording in progress.")

        self.parser = argparse.ArgumentParser(add_help=False)
        self.parser.add_argument(
            '-l', '--list-devices', action='store_true',
            help='show list of audio devices and exit')
        self.args, self.remaining = self.parser.parse_known_args()
        if self.args.list_devices:
            print(sd.query_devices())
            self.parser.exit(0)
        self.parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            parents=[self.parser])
        self.parser.add_argument(
            'channels', type=int, default=[1], nargs='*', metavar='CHANNEL',
            help='input channels to plot (default: the first)')
        self.parser.add_argument(
            '-d', '--device', type=self.check,
            help='input device (numeric ID or substring)')
        self.parser.add_argument(
            '-w', '--window', type=float, default=200, metavar='DURATION',
            help='visible time slot (default: %(default)s ms)')
        self.parser.add_argument(
            '-i', '--interval', type=float, default=30,
            help='minimum time between plot updates (default: %(default)s ms)')
        self.parser.add_argument(
            '-b', '--blocksize', type=int, help='block size (in samples)')
        self.parser.add_argument(
            '-r', '--samplerate', type=float, help='sampling rate of audio device')
        self.parser.add_argument(
            '-n', '--downsample', type=int, default=10, metavar='N',
            help='display every Nth sample (default: %(default)s)')
        self.args = self.parser.parse_args(self.remaining)
        if any(c < 1 for c in self.args.channels):
            self.parser.error('argument CHANNEL: must be >= 1')
        self.mapping = [c - 1 for c in self.args.channels]  # Channel numbers start with 1
        self.q = queue.Queue()

        self.plotdata = None
        
        try:
            if self.args.samplerate is None:
                device_info = sd.query_devices(self.args.device, 'input')
                self.args.samplerate = device_info['default_samplerate']

            length = int(self.args.window * self.args.samplerate / (1000 * self.args.downsample))
            self.plotdata = np.zeros((length, len(self.args.channels)))

            fig, ax = plt.subplots()
            self.lines = ax.plot(self.plotdata)
            if len(self.args.channels) > 1:
                ax.legend(['channel {}'.format(c) for c in self.args.channels],
                        loc='lower left', ncol=len(self.args.channels))
            ax.axis((0, len(self.plotdata), -1, 1))
            ax.set_yticks([0])
            ax.yaxis.grid(True)
            ax.tick_params(bottom=False, top=False, labelbottom=False,
                        right=False, left=False, labelleft=False)
            fig.tight_layout(pad=0)

            stream = sd.InputStream(
                device=self.args.device, channels=max(self.args.channels),
                samplerate=self.args.samplerate, callback=self.audio_cb)
            ani = FuncAnimation(fig, self.update_plot, interval=self.args.interval, blit=True)
            with stream:
                plt.show()
        except Exception as e:
            self.parser.exit(type(e).__name__ + ': ' + str(e))

        
        self.end = time.time()
        scrdControl.record = False
        print("Recording complete")
        self.myrecording = sd.rec(int((self.end-self.start) * self.fs), samplerate=self.fs, channels=2)
        sd.wait() 
        write('output.wav', self.fs, self.myrecording) 

