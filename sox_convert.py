#!/usr/bin/env python3

### Jonathan Rawlinson 2018 ###


import os, sys
import subprocess

import argparse

parser = argparse.ArgumentParser(description='### Converter of *.RAW GQRX recordings to SDR Sharp compatible recordings using SOX - Jonathan Rawlinson 2018 ###', epilog="For more help -->> SOX: http://sox.sourceforge.net/; GQRX: http://gqrx.dk/")

parser.add_argument('-a', help='Process all files in current directory', action="store_true")
parser.add_argument('-i', help='Process single file', action="store", dest="input_file")

args = parser.parse_args()

try:
    os.listdir("soxoutput/")
except FileNotFoundError:
    os.mkdir("soxoutput/")


def run_command(file_path):
    file_path_split = file_path.split(".")
    
    file_path_split_dirs = file_path_split[0].split("/")
    
    file_path_split_cf_fs = file_path_split[0].split("_")
    command = "sox -t raw -e floating-point -b 32 -c 2 -r %s %s %s" % (file_path_split_cf_fs[-2], file_path, "soxoutput/" + file_path_split_dirs[-1] + ".wav")
    print("Processing file %s with FS of %s Hz" % (file_path, file_path_split_cf_fs[-2]))
    print(command)
    os.system(command)

if args.a:
    input_files = os.listdir(".")
    for file_path in input_files:
        file_path_split = file_path.split(".")
        if (len(file_path_split) == 2):
            if (file_path_split[1] == "raw"):
                run_command(file_path)


if args.input_file == None:
    import tkinter as tk
    from tkinter import filedialog
    print("### Please setect a .RAW file for conversion ###")
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title = "Select Input File", filetypes = (("GQRX Recordings","*.raw"),("all files","*.*")))
    if len(file_path) == 0:
        print("No file setected, closing")
        sys.exit(0)
else:
    print("Reading %s" % args.input_file)
    file_path = args.input_file

run_command(file_path)

            

