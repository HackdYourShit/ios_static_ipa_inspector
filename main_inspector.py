#!/usr/bin/env python

from optparse import OptionParser
from target_class import TargetIpa
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

def UnzipFile():
    print("[+] unzip started \n")
    # zip_ref = zipfile.ZipFile(full_path, 'r')
    # zip_ref.extractall(directory_to_extract_to)
    # zip_ref.close()



if __name__ == '__main__':
    print("\n" + ('[+]' * 20) + ' script started ' + ('[+]' * 20) + "\n")
    target = TargetIpa()
    target.filename, target.file_and_path = Parameters()
    UnzipFile()
    print ("filepath:" + target.file_and_path)
    print ("filename:" + target.filename)