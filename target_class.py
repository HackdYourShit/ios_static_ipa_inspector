import os.path

class TargetIpa:
    def __init__(self):
        self.filename = "default"
        self.path = "default"
        self.unzipped_file_path = "default"
        self.time = 0

    @property
    def santized_path(self):
        if not self.path:
           return(os.getcwd())
        else:
            return(self.path)