def check_ten_path(ten_file):
    import os
    try:
        error_flag=False
        os.listdir(ten_file)
    except FileNotFoundError:
        print("Xin hay nhap lai ten path !!!")
        error_flag=True
    return ten_file, error_flag

import os

ten_file = input('Hay nhap ten file de kiem tra: ')
ten_file, error_flag = check_ten_path(ten_file)
#vi_tri_file = os.getcwd()
list_cac_file = os.listdir(ten_file)
print(list_cac_file)