import os

def create_temp_file(frame, index):
    temp_file = f'temp_{index}.png'
    frame.save(temp_file)
    return temp_file

def remove_temp_files(temp_files):
    for temp_file in temp_files:
        os.remove(temp_file)
