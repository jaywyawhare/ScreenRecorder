import subprocess

def encode_frames_to_video(frame_rate, output_file, temp_files):
    """
    Encode captured frames into a video using FFmpeg.

    Args:
        frame_rate (int): Number of frames per second for the output video.
        output_file (str): Output file name for the encoded video.
        temp_files (list): List of temporary file paths containing frames.

    Note:
        FFmpeg must be installed and accessible in the system's PATH.
    """
    ffmpeg_command = [
        'ffmpeg',
        '-y',
        '-framerate', str(frame_rate),
        '-i', 'temp_%d.png',
        '-c:v', 'libx264',
        '-crf', '18',
        '-pix_fmt', 'yuv420p',
        '-vf', 'pad=ceil(iw/2)*2:ceil(ih/2)*2',
        '-movflags', '+faststart',
        output_file
    ]

    subprocess.call(ffmpeg_command)
