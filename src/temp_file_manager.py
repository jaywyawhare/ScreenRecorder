import os

def create_temp_file(frame, index):
    """
    Create a temporary file to store a frame.

    Args:
        frame: The frame image to be saved.
        index (int): The index of the frame.

    Returns:
        str: The path to the created temporary file.
    """
    temp_file = f'temp_{index}.png'
    frame.save(temp_file)
    return temp_file

def remove_temp_files(temp_files):
    """
    Remove the specified temporary files.

    Args:
        temp_files (list): List of temporary file paths to be removed.
    """
    for temp_file in temp_files:
        os.remove(temp_file)
