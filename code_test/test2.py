import os

ten_file = input('Hay nhap ten file de kiem tra: ')
#vi_tri_file = os.getcwd()
list_cac_file = os.listdir(ten_file)
print(list_cac_file)