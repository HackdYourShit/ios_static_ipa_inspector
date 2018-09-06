#!/usr/bin/env python

from optparse import OptionParser
from target_class import TargetIpa
from thing_class import Thing
from r2_helper import CheckBinary
from log_printer import snappy_console_banner, snappy_console_print, snappy_console_arg_2
from pathlib import Path
import os.path
import zipfile

def Parameters():
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 0.1")
    parser.add_option("-a", "--assess",
                      dest="zipped_filename",
                      default=True,
                      help="Unzip and assess an iOS IPA file")
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("wrong number of arguments")

    path, filename = os.path.split(args[0])
    return(path, filename)

def UnzipFile(target_to_unzip):
    full_path = os.path.join(target_to_unzip.santized_path, target_to_unzip.filename)
    zipped_file = Path(full_path)
    print("[+] Checking file at path: " + full_path)

    try:
        result = zipped_file.exists()
    except FileNotFoundError:
        print("file not found")
    else:
        print("[+] file exist check: " + str(result))


if __name__ == '__main__':
    snappy_console_banner('script started')
    target = TargetIpa()
    target.path, target.filename = Parameters()
    UnzipFile(target)
    CheckBinary()
    a = Thing()
    a = ('odd','even','weird')
    snappy_console_print(a)

    # print a global List.