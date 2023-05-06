import os

vi_tri_file = os.getcwd()
list_cac_file = os.listdir(vi_tri_file)
ten_file = input('Hay nhap ten file de kiem tra: ')
ket_qua_kiem_tra_file = ten_file in list_cac_file
if ket_qua_kiem_tra_file == 1 :
    print('File', ten_file,'co ton tai va da bi xoa')
    os.remove(ten_file)
elif ket_qua_kiem_tra_file == 0 :
    print('File nay khong co ton tai trong folder.')