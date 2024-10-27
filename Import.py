from google.colab import drive
import os
import zipfile

# Mount Google Drive
drive.mount('/content/drive')

# Change directory to where the dataset is located
dataset_path = '/content/drive/MyDrive/path_to_your_dataset'  # Adjust to your specific path
os.listdir(dataset_path)
