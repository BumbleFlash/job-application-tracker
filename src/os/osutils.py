import os


class OsUtils:

    @staticmethod
    def create_directory_if_not_exists(directory_name):
        try:
            os.mkdir(directory_name)
        except OSError:
            print("Directory exists proceeding...")
