import os
import shutil

EXTRACTED_UNDERSCORES = []

folder = r"C:\Users\BARIAJB\Documents\Copy_underscore"

source = r"C:\Users\BARIAJB\Documents\Copy_underscore\{}"

destinationfolder = r"C:\Users\BARIAJB\Documents\copy_result_1"



for f in os.listdir(folder):
    if f.endswith('_1.jpg'):
        EXTRACTED_UNDERSCORES.append(f)
        shutil.copy(source.format(f), destinationfolder)

print("Number of copied _1 files: ", len(EXTRACTED_UNDERSCORES))
