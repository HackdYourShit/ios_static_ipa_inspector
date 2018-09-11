import os.path
from optparse import OptionParser

class YDStartUpParameters:

    def __init__ ( self, key, value ):
        self.key = key
        self.value = value

    @property
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
