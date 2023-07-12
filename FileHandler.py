import os
import shutil


class FileHandler:
    base_path = None
    working_directory = None

    @staticmethod
    def create_dir(path):
        os.mkdir(path)

    @classmethod
    def find_base_path(cls):
        current_directory = os.getcwd()
        while current_directory != '/':
            base_path = os.path.join(current_directory, '/.wit')
            if os.path.isdir(base_path):
                return base_path
            current_directory = os.path.dirname(current_directory)

        raise FileNotFoundError(".wit directory not found.")

    @classmethod
    def validate_path(cls, path):
        full_path = os.path.join(cls.working_directory, path)
        if not os.path.exists(full_path):
            raise Exception("the file dose not exists")
        return full_path

    @classmethod
    def copy_item(cls, origin, target):
        shutil.copy(origin, target)
