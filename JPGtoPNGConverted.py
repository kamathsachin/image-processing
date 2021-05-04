"""
Python script to read jpg files from a source folder 
and convert it into png and save in destination folder
"""

import sys
import os
from PIL import Image

# Read the source and destination folder names passed as arguments
source_folder = sys.argv[1]
destination_folder = sys.argv[2]

# Create a new destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through all the folder and convert the files to png and save in destination folder
for filename in os.listdir(source_folder):
    img = Image.open(f"{source_folder}{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save(f"{destination_folder}{clean_name}.png", "png")

print("Converted All Files")
