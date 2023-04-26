import shutil
import os

EXTRACTED_UNDERSCORE1 = []
EXTRACTED_UNDERSCORE2 = []
EXTRACTED_UNDERSCORE3 = []

ShopeeFolder = r""
LazadaFolder = r""
ZaloraFolder = r""

folder = r"C:\Users\BARIAJB\Documents\Copy_underscore"
source = r"{}\{}"
destinationfolder1 = r"C:\Users\BARIAJB\Documents\copy_result_1"
destinationfolder2 = r"C:\Users\BARIAJB\Documents\copy_result_2"
destinationfolder3 = r"C:\Users\BARIAJB\Documents\copy_result_3"

for f in os.listdir(folder):
    if f.startswith("_1.txt.txt"):
        EXTRACTED_UNDERSCORE1.append(f)
        shutil.copy(source.format(folder, f), destinationfolder1)
    elif f.endswith("_2.txt.txt"):
        EXTRACTED_UNDERSCORE2.append(f)
        shutil.copy(source.format(folder, f), destinationfolder2)

    elif f.endswith("_3.txt.txt"):
        EXTRACTED_UNDERSCORE3.append(f)
        shutil.copy(source.format(folder, f), destinationfolder3)

print("Number of copied _1 files: ", len(EXTRACTED_UNDERSCORE1))
print("Number of copied _2 files: ", len(EXTRACTED_UNDERSCORE2))
print("Number of copied _3 files: ", len(EXTRACTED_UNDERSCORE3))
