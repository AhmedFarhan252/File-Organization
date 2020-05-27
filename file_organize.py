import os
import zipfile
from pathlib import Path
from pTable import print_table

home = Path.home()
cd = Path.cwd()


def print_dir(cd, selected_folder):
    dir = cd / selected_folder

    for folder, subfolder, filename in os.walk(dir):
        # divide path by each directory into list
        dir_split = folder.split(os.path.sep)

        # get index after selected folder in list
        i = 0
        for (idx, val) in enumerate(dir_split):
            if val == selected_folder:
                i = idx
                break

        if (i != len(dir_split)):
            path = "Directory : " + str(os.path.join(*dir_split[i:]))
            print(path)

            path_size = len(path)
            folder_name = len(folder.split(os.path.sep)[-1])
            spaces = path_size - folder_name - 1

            for x in subfolder:
                print(" " * spaces + " |-> ", x)

            for x in filename:
                print(" " * spaces + " |-> ", x)

            print("")


def read_zip(fname):
    reader = zipfile.ZipFile(cd / fname)

    col = ['Name', 'Size (Bytes)', 'Compressed Size (Bytes)',
           'Compression Percentage']
    val = []
    for x in reader.namelist():
        row = []

        fileinfo = reader.getinfo(x)
        file_size = fileinfo.file_size
        compress_size = fileinfo.compress_size

        row.append(x)
        row.append(str(file_size))
        row.append(str(compress_size))

        if compress_size == 0:
            row.append("0 %")
        else:
            row.append(
                str(round((file_size-compress_size)/file_size * 100, 2)) + " %")

        val.append(row)

    print_table(val, col)
    reader.close()
