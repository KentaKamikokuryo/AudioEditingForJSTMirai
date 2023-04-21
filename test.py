from classes.path_info import PathInfo
from classes.utilitiesfile import UtilitiesFile
from pathlib import Path
import srt

path_info = PathInfo()
NUM = 1
path_dict = path_info.get_path_dict(num=NUM)

subs = UtilitiesFile.get_subtitles_from_srt(srt_path=path_dict["srt"], is_show_console=True)
list_line = UtilitiesFile.get_strlist_from_txt(txt_path=path_dict["txt"], is_show_console=False)
