def check_ten_path(vi_tri_file):
    import os
    try:
        error_flag=False
        os.listdir(vi_tri_file)
    except FileNotFoundError:
        print("Xin hay nhap lai ten path !!!")
        error_flag=True
    return vi_tri_file, error_flag
import os
#----------------------------------------------------------------------
#Nhap du lieu file path va file name, gan error_flag
vi_tri_file = input('Hay nhap file path: ')
vi_tri_file, error_flag = check_ten_path(vi_tri_file)
list_cac_file = os.listdir(vi_tri_file)
ten_file = input('Hay nhap ten file de kiem tra: ')
#----------------------------------------------------------------------
#kiem tra xem file co ton tai hay khong
ket_qua_kiem_tra_file = ten_file in list_cac_file
if ket_qua_kiem_tra_file == 1 :
    print('File', ten_file,'co ton tai va da bi xoa')
    os.remove(ten_file)
elif ket_qua_kiem_tra_file == 0 :
    print('File nay khong co ton tai trong folder.')