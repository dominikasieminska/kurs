import os
import os.path

def przegladanie(root):
    file_list = os.listdir(root)
    dir_list = []
    pliki_wg_rozmiaru = {'rozmiar' : 'plik'}

    for item in file_list:
        if os.path.isfile(os.path.join(root, item)):
            full_name = os.path.join(root, item)
            file_size = os.path.getsize(full_name)
            print(full_name, file_size)

            pliki_wg_rozmiaru[file_size] = full_name

        if os.path.isdir(os.path.join(root, item)):
            dir_list.append(item)
    for dirname in dir_list:
        przegladanie(os.path.join(root, dirname))

    return pliki_wg_rozmiaru


print(przegladanie('.'))

