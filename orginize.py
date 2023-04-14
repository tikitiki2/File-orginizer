
import os
from depend import funcs as f

# focus on creating the program through commandline first then create the GUI no need to create gui until done make


#file type or extension
filetype_ext=input('enter the kind of file you would like to organize or enter a specific file extension such as .mp3: ').lower()

ftype=f.get_file_type(filetype_ext) # returns tuple with 2 elements if starts with . and 3 if not
#example output ('category', 'images', ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'])

directory=input('enter full directory of where to cleanup enter nothing to use current directory: ')
# ask for permission to enter files in directory and look into those files recursively
check_files=input('go into all files in directory Y/N: ').lower()  # lower for consistency
if check_files=='y':
    check_files = True
    try:
        limit=int(input('enter depth limit enter nothing for no limit: '))
    except Exception as e:
        print(e)
        exit(1)
    if not limit:
        limit=None
else:
    check_files=False
    limit = None
if not directory:
    #default directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if not os.path.isdir(dir_path):
         print(f'invalid directory {directory}')
         exit(1)
    else:
        f.move(dir_path=dir_path, file_info=ftype,check_files=check_files,limit=limit)
else:
    if not os.path.isdir(directory):
         print(f'invalid directory {directory}')
         exit(1)
    else:
        f.move(dir_path=directory,file_info=ftype,check_files=check_files,limit=limit)

#todo upload to github






