#!/usr/bin/env python

from yd_console import YDConsole
from yd_radare2 import CheckBinary
from yd_file_ext_search import YDFileExtensionSearch
from yd_start_helper import YDStartUpParameters
from yd_version import YDVersion

if __name__ == '__main__':
    y = ('script started: ' + '\t' + YDVersion.string())
    YDConsole.banner(y)


    b = YDStartUpParameters()
    print(b)


    a = YDFileExtensionSearch("")
    YDFileExtensionSearch.list_files(a)