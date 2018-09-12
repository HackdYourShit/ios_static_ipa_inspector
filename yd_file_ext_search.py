#!/usr/bin/env python

import os
from yd_console import YDConsole
from enum import Enum

class YDDepth(Enum):
    HEAVY = 1
    LIGHT = 0

class YDFileExtensionSearch:

    def __init__ ( self, root_directory, log_depth:YDDepth ):
        self.root_directory = root_directory
        self.log_level = log_depth
        self.directory_extensions = ['framework', 'bundle']
        self.file_extensions_light = ['json','cert','crt','html','js', 'cer', 'pub']
        self.file_extensions_deep = ['plist','strings']
        self.list_files()

    def __str__ ( self ):
        return "Log level " + str(self.log_level)

    def list_files(self):

        extension_final = self.file_extensions_light
        if self.log_level == YDDepth.HEAVY:
            extension_final =  self.file_extensions_light + self.file_extensions_deep

        for i in extension_final:
            YDConsole.banner('Looking for: ' + i)
            for root, dirs, files in os.walk(self.root_directory):
                for f in files:
                    if f.endswith(i):
                        YDConsole.single_value_subheading(f)
        return None

    def list_frameworks(self):
        for i in self.directory_extensions:
            YDConsole.banner('Looking for: ' + i)
            for root, dirs, files in os.walk(self.root_directory):
                for d in dirs:
                    if d.endswith(i):
                        YDConsole.single_value_subheading(d)

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