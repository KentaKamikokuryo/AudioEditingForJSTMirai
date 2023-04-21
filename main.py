from classes.path_info import PathInfo
from classes.utilitiesfile import UtilitiesFile, UtilitiesAudioEditing

path_info = PathInfo()
nums = [1, 2]

for NUM in nums:

    path_dict = path_info.get_path_dict(num=NUM)

    subs = UtilitiesFile.get_subtitles_from_srt(srt_path=path_dict["srt"], is_show_console=False)
    list_line = UtilitiesFile.get_strlist_from_txt(txt_path=path_dict["txt"], is_show_console=False)

    content_list = []
    for i, sub in enumerate(subs):

        index = sub.index
        time_start = sub.start
        time_end = sub.end

        if i == 0:
            print("start audio editing")

        elif content_list[-1] == sub.content:
            print("skip the index: {}".format(index))

        else:
            UtilitiesAudioEditing.cut_output_stream(video_path=path_dict["audio"], index=index,
                                                    start=time_start, end=time_end, save_path=path_info.result_folder)

        content_list.append(sub.content)


