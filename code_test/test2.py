
import os
def check_ten_path(ten_file):
    import os
    try:
        error_flag=False
        os.listdir(ten_file)
    except :
        print('hi')

ten_file = input('Hay nhap ten file de kiem tra: ')
#vi_tri_file = os.getcwd()
list_cac_file = os.listdir(ten_file)
print(list_cac_file)