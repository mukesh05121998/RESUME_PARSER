import os

class FileTypeIdentifier:
    def __init__(self, file_path):
        self.file_path = file_path

    def identify_file_type(self):
        if not os.path.isfile(self.file_path):
            return None
        file_extension = os.path.splitext(self.file_path)[1]
        return file_extension
