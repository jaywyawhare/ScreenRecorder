import subprocess

def encode_frames_to_video(frame_rate, output_file, temp_files):
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
