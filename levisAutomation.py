import os
import shutil

EXTRACTEDBARCODEFILES = []

folder = r"C:\Users\Owner\Desktop\Testfolderbarcodesource"

source = r"C:\Users\Owner\Desktop\Testfolderbarcodesource\{}"

destinationfolder = r"C:\Users\Owner\Desktop\Barcodefiles_Test"

for f in os.listdir(folder):
    if f.endswith('BARCODE.jpg') or f.endswith('barcode.jpg') or f.endswith('Barcode.jpg'):
        EXTRACTEDBARCODEFILES.append(f)
        shutil.move(source.format(f), destinationfolder)

print("Number of extracted barcode files: ", len(EXTRACTEDBARCODEFILES))