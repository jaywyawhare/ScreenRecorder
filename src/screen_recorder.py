import tkinter as tk
from datetime import datetime
from temp_file_manager import create_temp_file, remove_temp_files
from ffmpeg_encoder import encode_frames_to_video
import pyscreenshot as ImageGrab
import time

class ScreenRecorderApp:
    def __init__(self, frame_rate, output_file):
        """
        Initialize the ScreenRecorderApp.

        Args:
            frame_rate (int): Number of frames per second to record.
            output_file (str): Output file name for the recorded video.
        """
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
        """
        Start the screen recording.
        """
        self.recording = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.capture_screen()

    def stop_recording(self):
        """
        Stop the screen recording and encode frames into a video file.
        """
        self.recording = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.encode_frames_to_video()

    def capture_screen(self):
        """
        Continuously capture screenshots while recording is enabled.
        """
        while self.recording:
            start_time = time.time()

            screenshot = ImageGrab.grab()
            self.frames.append(screenshot)
            self.root.update()

            elapsed_time = time.time() - start_time
            sleep_duration = max(0, (1.0 / self.frame_rate) - elapsed_time)
            time.sleep(sleep_duration)

    def encode_frames_to_video(self):
        """
        Encode captured frames into a video file.
        """
        temp_files = []
        for i, frame in enumerate(self.frames):
            temp_file = create_temp_file(frame, i)
            temp_files.append(temp_file)

        encode_frames_to_video(self.frame_rate, self.output_file, temp_files)

        remove_temp_files(temp_files)

def main():
    """
    Main entry point of the program.
    """
    frame_rate = 5

    now = datetime.now()
    date_time = now.strftime("%H%M%d%m%y")

    output_file = f'screen_recording_{date_time}.mkv'

    app = ScreenRecorderApp(frame_rate, output_file)

if __name__ == "__main__":
    main()
