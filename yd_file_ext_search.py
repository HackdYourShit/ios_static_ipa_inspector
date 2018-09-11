#!/usr/bin/env python

import os

class FileExtensionSearch:

    def __init__ ( self, root_directory ):
        self.root_directory = root_directory

    def ListFiles(directory):
        "Search for files inside the iPA that gives clues about how it works"
        file_extensions = ['.json', '.cert', '.crt', ]  # 'plist' can return lots of results
        directory_extensions = ['framework', 'bundle']
        print("[+] Looking for extension: " + str(file_extensions))
        print("[+] Looking in directory: " + directory)

        for root, dirs, files in os.walk(directory):
            for d in dirs:
                if d.endswith(tuple(directory_extensions)):
                    print("[+] found -> " + os.path.join(root, d))

            for f in files:
                if f.endswith(tuple(file_extensions)):
                    print("[+] found -> " + os.path.join(root, f))

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