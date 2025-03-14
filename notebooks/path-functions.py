import os
from os import path
from dotenv import load_dotenv


def trainPath():
    """
    Returns the relative path containing training datasets, specificed by environment variables.
    """

    return os.path.join(os.getenv("DATASET_LOCATION"), os.getenv("TRAIN_LOCATION"))


def testPath():
    """
    Returns the relative path containing testing datasets, specificed by environment variables.
    """
    return os.path.join(os.getenv("DATASET_LOCATION"), os.getenv("TEST_LOCATION"))


def datasetPath():
    """
    Returns the relative path containing all datasets, specificed by environment variables.
    """

    return os.getenv("DATASET_LOCATION")


if __name__ == "__main__":
    print(f'Training path:\t\t"{trainPath():>}"')
    print(f'Testing path:\t\t"{testPath():>}"')
    print(f'General dataset path:\t"{datasetPath():>}"')
