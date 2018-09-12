import os.path
from optparse import OptionParser
from yd_error_handling import YDErrorHandling
import sys

class YDStartUpParameters:

    path = sys.argv[1]
    count = len(sys.argv[1:])

    def __init__ (self):
        self.validate_count()
        self.validate_path()

    def __str__ ( self ):
        return self.path

    def validate_count ( self ):
        if self.count != 1:
            YDErrorHandling.exit_on_usage(self)

    def validate_path(self):
        if os.path.isdir(self.path) == False:
            YDErrorHandling.exit_on_usage(self.path)

        #
   #     path, filename = os.path.split(args[0])