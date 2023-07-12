import datetime
import os
import secrets
from FileHandler import *

class Commit:
    @staticmethod
    def get_hash_name():
        commit_id = secrets.token_hex(20)
        return commit_id

    @staticmethod
    def make_dir_in_imges( commit_id, path):
        full_path = os.path.join(path, commit_id)
        FileHandler.create_dir(full_path)
        os.

    make_dir_in_imges(get_hash_name(), os.path.join(, "/wit/images"))
    def make_metadata_file(commit_id, path, message):
        f = open(f"{commit_id}.txt", "w+")
        f.write(f"""
        parent = {None}
        date = {datetime.time}
        message = {message}
        """)
        f.close()
