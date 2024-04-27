import os
import shutil

def rename_files_in_folder(folder_path, separator):
    """
    This program copies files in folder to root folder 
    and renames them according to their file path.
    """
    folders = [folder_path+"/"+i for i in os.listdir(folder_path)]
    sys_file = "/".join([folder_path, ".DS_Store"])
    if sys_file in folders:
        folders.remove("/".join([folder_path, ".DS_Store"]))
    print("_______")
    for i in folders:
        for j in os.listdir(i):
            shutil.copy("/".join([i,j]), \
            "/".join([folder_path, "_".join([i[i.rfind(separator):],j])]))

rename_files_in_folder("/Users/sanakulov/wdir/tickets copy", "PLANREPBA")