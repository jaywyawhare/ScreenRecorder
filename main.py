import pyscreenshot as ImageGrab
import subprocess
import os
import time
import tkinter as tk
from datetime import datetime

class ScreenRecorderApp:
    def __init__(self, frame_rate, output_file):
        self.frame_rate = frame_rate
        self.output_file = output_file
        self.frames = []
        self.recording = False
        self.root = tk.Tk()
        self.root.title("Screen Recorder")
        self.start_button = tk.Button(self.root, text="Start Recording", command=self.start_recording)
        self.start_button.pack(pady=10)
        self.stop_button = tk.Button(self.root, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(pady=5)
        self.root.mainloop()

    def start_recording(self):
        self.recording = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.capture_screen()

    def stop_recording(self):
        self.recording = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.encode_frames_to_video()

    def capture_screen(self):
        while self.recording:
            start_time = time.time()

            screenshot = ImageGrab.grab()
            self.frames.append(screenshot)
            self.root.update()

            elapsed_time = time.time() - start_time
            sleep_duration = max(0, (1.0 / self.frame_rate) - elapsed_time)
            time.sleep(sleep_duration)


    def encode_frames_to_video(self):
        temp_files = []
        for i, frame in enumerate(self.frames):
            temp_file = f'temp_{i}.png'
            frame.save(temp_file)
            temp_files.append(temp_file)

        ffmpeg_command = [
            'ffmpeg',
            '-y',
            '-framerate', str(self.frame_rate),
            '-i', 'temp_%d.png',
            '-c:v', 'libx264',
            '-crf', '18',
            '-pix_fmt', 'yuv420p',
            '-vf', 'pad=ceil(iw/2)*2:ceil(ih/2)*2',
            '-movflags', '+faststart',
            output_file
        ]

        subprocess.call(ffmpeg_command)

        for temp_file in temp_files:
            os.remove(temp_file)


frame_rate = 3 

now = datetime.now()
date_time = now.strftime("%H%M%d%m%y")

output_file = f'screen_recording_{date_time}.mkv'

app = ScreenRecorderApp(frame_rate, output_file)
