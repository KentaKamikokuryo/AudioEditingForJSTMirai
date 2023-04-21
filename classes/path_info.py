import os
import sys
from pathlib import Path


class PathInfo():

    def __init__(self, path_parent=None):

        if path_parent is None:
            self.path_parent_project = os.getcwd()

        else:
            self.path_parent_project = path_parent

        print("The parent path is got from {}".format(self.path_parent_project))

        # 現在のパスを上の階層に上げ、データフォルダに移動する。
        os.chdir("..")
        self.path_data = os.getcwd() + "\\23_03_08__01-02\\23_03_08__01-02\\"
        print("The data is obtained from {}".format(self.path_data))

        self.result_folder = ""
        self._set_path_data_child()

    def _set_path_data_child(self):

        self.path_data_1 = self.path_data + "01\\"
        self.path_data_2 = self.path_data + "02\\"
        print("The options to get data are {} and {}".format("01", "02"))

    def get_path_dict(self, num: int = 1):

        data_dict = {}

        if num == 1:

            data_dict = {"audio": self.path_data_1 + "230308_1312.mp3",
                         "srt": self.path_data_1 + "230308_1312.mp3.srt",
                         "txt": self.path_data_1 + "230308_1312.mp3.txt",
                         "vtt": self.path_data_1 + "230308_1312.mp3.vtt"}

            self.result_folder = self.path_data_1 + Path(data_dict["audio"]).stem + "\\"

        elif num == 2:

            data_dict = {"audio": self.path_data_2 + "230308_1301.mp3",
                         "srt": self.path_data_2 + "230308_1301.mp3.srt",
                         "txt": self.path_data_2 + "230308_1301.mp3.txt",
                         "vtt": self.path_data_2 + "230308_1301.mp3.vtt"}

            self.result_folder = self.path_data_2 + Path(data_dict["audio"]).stem + "\\"

        else:

            print("The number is not found.")
            raise FileNotFoundError

        print("The audio file is in {}".format(data_dict["audio"]))
        if not os.path.exists(self.result_folder):
            os.makedirs(self.result_folder)
        print("The result folder is in {}".format(self.result_folder))

        return data_dict
