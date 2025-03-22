import os
import datetime
from os import path
from dotenv import load_dotenv
import matplotlib.pyplot as plt


def trainPath(file_name=None):
    """
    Get the relative path for training datasets, specified by environment variables.

    Arguments:
        file_name (str): (Optional) Name of the file
    Returns:
        out (str): Path to the file in the training directory, if a filename was provided. Otherwise, path to the training directory itself.
    """
    if file_name == None:
        return os.path.join(os.getenv("TRAIN_LOCATION"))
    else:
        return os.path.join(os.getenv("TRAIN_LOCATION"), file_name)


def testPath(file_name=None):
    """
    Get the relative path for testing datasets, specified by environment variables.

    Arguments:
        file_name (str): (Optional) Name of the file
    Returns:
        out (str): Path to the file in the testing directory, if a filename was provided. Otherwise, path to the testing directory itself.
    """
    if file_name == None:
        return os.path.join(os.getenv("TEST_LOCATION"))
    else:
        return os.path.join(os.getenv("TEST_LOCATION"), file_name)


def datasetPath(file_name=None):
    """
    Get the relative path to all datasets, specified by environment variables.

    Arguments:
        file_name (str): (Optional) Name of the file
    Returns:
        out (str): Path to the file in datasets directory, if a filename was provided. Otherwise, path to the datasets directory itself.
    """
    if file_name == None:
        return os.getenv("DATASET_LOCATION")
    else:
        return os.path.join(os.getenv("DATASET_LOCATION"), file_name)


def mountColab():
    """
    Mount the Google Colab drive, specified by environment variables

    Returns:
     out (bool) : True if mounted successfully
    """
    try:
        from google.colab import drive

        drive.mount(os.getenv("COLAB_DIR"))
    except:
        print(f'Could not find google drive mount "{os.getenv("COLAB_DIR")}"')


def imgPath(file_name=None):
    """
    Get the relative path to saved images, specified by environment variables.

    Arguments:
        file_name (str): (Optional) Name of the file
    Returns:
        out (str): Path to the file in images directory, if a filename was provided. Otherwise, path to the images directory itself.
    """
    if file_name == None:
        return os.getenv("IMAGE_SAVE_LOC")
    else:
        return os.path.join(os.getenv("IMAGE_SAVE_LOC"), file_name)


if __name__ == "__main__":
    print(f'Training path:\t\t"{trainPath():>}"')
    print(f'Testing path:\t\t"{testPath():>}"')
    print(f'General dataset path:\t"{datasetPath():>}"')
    print(f"Img")
