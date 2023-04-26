import os
import shutil


# set variable for master source file
master_file = r"C:\Users\BARIAJB\Documents\master_file"
set_source = r"{}/{}"
master_file_list = []

Shopee_Lazada_list = ['item1.txt', 'item2.txt', 'item3.txt', 'item4.txt']
ZaloraList = ['item5.rtf', 'item6.txt']


Shopee_lazada_new = r"C:\Users\BARIAJB\Documents\Shopee_lazada_new"
Zalora_New = r"C:\Users\BARIAJB\Documents\Zalora_New"

ConfirmedLIstSL = []
ConfirmedLIstZal = []

# get list of shopee jpg and lazada jpg

for f in os.listdir(master_file):
    master_file_list.append(f)


for sl in Shopee_Lazada_list:
    if sl in master_file_list:
        ConfirmedLIstSL.append(sl)
        shutil.copy(set_source.format(master_file, sl), Shopee_lazada_new)

#
for zal in ZaloraList:
    if zal in master_file_list:
        ConfirmedLIstZal.append(zal)
        shutil.copy(set_source.format(master_file, zal), Zalora_New)
#
#
#
for f in os.listdir(Shopee_lazada_new):
    ConfirmedLIstSL.append(f)

#
for f in os.listdir(Zalora_New):
    ConfirmedLIstZal.append(f)

#
all_confirmed = ConfirmedLIstSL + ConfirmedLIstZal
#
list_of_unidentified = []

print("List of Unidentified files:")

for u in master_file_list:
    if u not in all_confirmed:
        list_of_unidentified.append(u)

        print(u)



