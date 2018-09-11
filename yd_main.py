#!/usr/bin/env python

from yd_console import YDConsole
from yd_radare2 import CheckBinary
from yd_file_ext_search import FileExtensionSearch
from yd_parameters import YDStartUpParameters
from yd_version import YDVersion

if __name__ == '__main__':
    YDConsole.banner('script started')
    # CheckBinary()

    print(YDVersion.string())
    a = FileExtensionSearch("/home")
    print(a.root_directory)
