#!/usr/bin/env python

import os.path
from optparse import OptionParser
from yd_console import YDConsole
from yd_radare2 import CheckBinary


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




if __name__ == '__main__':
    YDConsole.banner('script started')
    CheckBinary()
