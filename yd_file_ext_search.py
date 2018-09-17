#!/usr/bin/env python
import glob
import os
from yd_console import YDConsole
from yd_error_handling import YDErrorHandling
from enum import Enum

class YDDepth(Enum):
    HEAVY = 1
    LIGHT = 0

class YDFileExtensionSearch:

    def __init__ ( self, root_directory, log_depth:YDDepth ):
        self.root_directory = root_directory

        if self.root_directory:
            self.app_bundle_dir = self.return_app_bundle()

        self.log_level = log_depth
        self.general_settings = ['CFBundleName', 'CFBundleExecutable', 'CFBundleIdentifier', 'MinimumOSVersion',
                                 'UILaunchStoryboardName']
        self.directory_extensions = ['framework','bundle','storyboardc']
        self.file_extensions_light = ['json','cert','crt','html','js','cer','pub','txt']
        self.file_extensions_deep = ['plist','strings']
        self.target_permissions = ['framework','bundle','storyboardc']

        if self.log_level == YDDepth.HEAVY:
            self.list_files()
            self.list_frameworks()
            self.inspect_info_plist()
        else:
            self.list_files()
            self.inspect_info_plist()

    def __str__ ( self ):
        return "Log level " + str(self.log_level)

    def return_app_bundle( self ):
        plist_hunt= os.path.join(self.root_directory + '/*.app')
        for i in glob.glob(plist_hunt):
            YDConsole.single_label_and_value('Found app bundle name', os.path.basename(i))
            return i
        YDErrorHandling.exit_on_usage('no app bundle name found')

    def list_files(self):

        extension_final = self.file_extensions_light
        if self.log_level == YDDepth.HEAVY:
            extension_final =  self.file_extensions_light + self.file_extensions_deep

        for i in extension_final:
            YDConsole.banner('Looking for: ' + i)
            for root, dirs, files in os.walk(self.root_directory):
                for f in files:
                    if f.endswith(i):
                        YDConsole.single_value_subheading(os.path.join(root, f))
        return None

    def list_frameworks(self):
        for i in self.directory_extensions:
            YDConsole.banner('Looking for: ' + i)
            for root, dirs, files in os.walk(self.root_directory):
                for d in dirs:
                    if d.endswith(i):
                        YDConsole.single_value_subheading(d)

        return None


    def inspect_info_plist(self):

        target_infoplist = self.app_bundle_dir + '/Info.plist'
        if os.path.isfile(target_infoplist) == True:
            YDConsole.single_label_and_value('Searching plist',target_infoplist)

        try:
            import plistlib
        except ImportError:
            return None

        with open(target_infoplist, 'rb') as f:
            pl = plistlib.load(f)

        temp_permission_dict = {}  # added to avoid mix up of Permissions and Settings
        YDConsole.banner('General info from Info.plist')
        for key, value in pl.items():
            if key in self.general_settings:
                YDConsole.single_label_and_value(key, value)
            if key.startswith('NS'):
                temp_permission_dict[key] = value

        YDConsole.banner('User Permissions')
        for iv, ik in temp_permission_dict.items():
            YDConsole.single_label_and_value(iv, ik)

        return None
