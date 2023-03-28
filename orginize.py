
import os
from depend import funcs as f




#file type or extension
filetype_ext=input('enter the kind of file you would like to organize or enter a specific file extension such as .mp3: ').lower()
#calls funcs dependancy where validation also happens
ftype=f.get_file_type(filetype_ext) # returns tuple with 2 elements if starts with . and 3 if not
#example output ('category', 'images', ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'])

directory=input('enter full directory of where to cleanup enter nothing to use current directory: ')

if not directory:
    #default directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if not os.path.isdir(dir_path):
         print(f'invalid directory {directory}')
         exit(1)
    elif ftype[0]=='extension':
        # is a file extension
        f.move(dir_path=dir_path,file_type=ftype[1],extension=filetype_ext)
        pass
    elif ftype[0]=='category':
        #is a category of files
        f.move(dir_path=dir_path,file_type=ftype[1],li=ftype[2])
        pass
    else:
        print('unkown error, how did you get here this is not possible')
        exit(1)
else:
    if not os.path.isdir(directory):
         print(f'invalid directory {directory}')
         exit(1)
    elif ftype[0]=='extension':
        # is a file extension
        f.move(dir_path=directory,file_type=ftype[1],extension=filetype_ext)
        pass
    elif ftype[0]=='category':
        #is a category of files
        f.move(dir_path=directory,file_type=ftype[1],li=ftype[2])
        pass
    else:
        print('unkown error, how did you get here this is not possible')
        exit(1)



