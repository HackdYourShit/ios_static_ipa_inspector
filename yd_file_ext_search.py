#!/usr/bin/env python

import os
from yd_console import YDConsole

class YDFileExtensionSearch:

    def __init__ ( self, root_directory ):
        self.root_directory = root_directory

    @staticmethod
    def list_files(self):
        file_extensions = ['.json', '.cert', '.crt', ]  # 'plist' can return lots of results
        YDConsole.single_label_and_value("Looking for extension", str(file_extensions))

        for root, dirs, files in os.walk(self.root_directory):
            for f in files:
                if f.endswith(tuple(file_extensions)):
                    print("[+] found -> " + os.path.join(root, f))
        return None


    @staticmethod
    def list_frameworks(self):
        directory_extensions = ['framework', 'bundle']
        YDConsole.single_label_and_value('Looking in directory' , self.root_directory)

        for root, dirs, files in os.walk(self.root_directory):
            for d in dirs:
                if d.endswith(tuple(directory_extensions)):
                    print("[+] found -> " + os.path.join(root, d))
        return None


    def ReadInfoPlist(directory):
        plist_file = os.path.join(directory, 'Info.plist')
        print("[+] HUNT -> " + plist_file)
        try:
            f = open(plist_file, 'rb')
        except IOError:
            print
            "Could not read file:", fname

        with f:
            reader = csv.reader(f)
            for row in reader:
                pass  # do stuff here

        return None