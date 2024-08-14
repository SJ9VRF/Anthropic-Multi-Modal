# Module to load images from the filesystem.
from PIL import Image
from llama_index.core import SimpleDirectoryReader

def load_image(path):
    return Image.open(path)

def load_directory_images(directory_path):
    return SimpleDirectoryReader(input_files=[directory_path]).load_data()
