import shutil
import os
from depend import filetypes as ft
global count
count=0

def move(dir_path, file_info ,check_files=False,limit=None):
    #file_info= ('category', 'images', ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'])
    if not os.path.isdir(dir_path+f'\\{file_info[1]}'):
        os.mkdir(dir_path+f'\\{file_info[1]}')

    new_dir=dir_path+f'\\{file_info[1]}'
    if file_info[0]=='category':
        blackbox(dir_path,file_info[2],new_dir,check_files,limit=limit)
    else:
        blackbox(dir_path,[file_info[1]],new_dir,check_files,limit=limit)

def blackbox(full_path,ext,move_to,check_file=False,limit=None,cur_depth=0):
    if limit!=None:
        if cur_depth>=limit:
            print(f'reached max depth at {full_path}')
            return
    for file in os.scandir(full_path):
        if file.name.endswith(tuple(ext)):
            print(file.name)
            if os.path.exists(f'{move_to}\\{file.name}'): # https://docs.python.org/3/library/os.path.html?highlight=exists#os.path.exists
                print(f'duplicate file found {file.name}')
                new_name=rename(file.path)
                os.rename(file.path,new_name)

                shutil.move(new_name, move_to)
            else:
                shutil.move(file.path,move_to)
        elif check_file:
            if file.is_dir(follow_symlinks=True):
                print(f'directory found --> {file.name}')
                blackbox(file.path, ext, move_to, check_file,limit=limit,cur_depth=cur_depth+1)


#rename duplicate files
def rename(file_path):
    global count
    ext=''
    index=len(file_path)
    for i in range(len(file_path)-1,0,-1):
        if file_path[i]=='.':
            ext=file_path[i::]
            index=i
        elif file_path[i]=='\\':
            path=file_path[0:i+1]
            fname=file_path[i+1:index]
            break
    count+=1
    new_path=path+fname+f'({count})'+ext
    return new_path

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
