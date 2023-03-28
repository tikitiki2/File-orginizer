import shutil
import os
import filetypes as ft
#pass in directory to clean up and file extension type
def move(dir_path,file_type=None,extension=None,li=None):

    #check if folder exists
    if extension:
        if not os.path.isdir(dir_path + f'\\{file_type[1::]}'):
            os.mkdir(dir_path + f'\\{file_type[1::]}')
        for file in os.scandir(dir_path):
            file_name = file.name
            if file_name.endswith(extension):
                print(file_name)
                shutil.move(os.path.join(dir_path, file_name), os.path.join(dir_path, file_type[1:]))
    else:
        if not os.path.isdir(dir_path + f'\\{file_type}'):
            os.mkdir(dir_path + f'\\{file_type}')
        for file in os.scandir(dir_path):
            file_name = file.name
            ext=file_name[file_name.rfind('.') + 1:]

            if '.'+ext in li:
                print(file_name)
                shutil.move(os.path.join(dir_path, file_name), os.path.join(dir_path, file_type))


def get_file_type(filetype_ext):
    if not filetype_ext:
        print('no input detected')
        return exit(1)
    elif filetype_ext.startswith('.'):
        #check if valid/supported file extension
        if check(filetype_ext):
        # return a tuple with the type extension and the actual file extension
            return ('extension',filetype_ext)
        print(f'invalid extension type {filetype_ext}')
        return exit(1)
    else:
        if filetype_ext in ft.types:
            return ('category',ft.types[ft.types.index(filetype_ext)],get_li(ft.types[ft.types.index(filetype_ext)]))
        print(f'invalid file type {filetype_ext}')
        return exit(1)

def check(extension):
    for i in [ft.extensions['code'],ft.extensions['audio'],ft.extensions['video'],ft.extensions['image'],ft.extensions['document']]:
        for j in i:
            if j==extension:
                #found valid extension
                return True
    #file extension is invalid
    return False
def get_li(file_type):
    if file_type.endswith('s'):
        return ft.extensions[file_type[:-1]]
    return ft.extensions[file_type]
