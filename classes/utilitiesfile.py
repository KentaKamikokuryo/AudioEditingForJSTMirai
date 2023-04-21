import srt
import ffmpeg


class UtilitiesFile():

    @staticmethod
    def get_subtitles_from_srt(srt_path: str = None, is_show_console: bool = False):
        """
        サブタイトルを出力するためのユーティリティ関数
        :param srt_path:
        :param is_show_console:
        :return:
        """
        if srt_path is None:
            return

        with open(srt_path, mode="r", encoding="utf-8") as f:

            subs = srt.parse(f.read())

            if is_show_console:
                for sub in subs:
                    print(sub)

        """
        値を取り出すときは、次のように取り出す。
        for sub in subs: 
            print(sub.index) 
            print(sub.start) 
            print(sub.end) 
            print(sub.content)
        """
        print("The data as SRT have been gotten from PATH: {}".format(srt_path))
        return subs

    @staticmethod
    def get_strlist_from_txt(txt_path: str = None, is_show_console: bool = False):
        """
        strのリストを取り出す関数
        :param txt_path:
        :param is_show_console:
        :return:
        """

        if txt_path is None:
            return

        with open(txt_path, encoding="utf-8") as f:

            lines = f.read()
            list_line = []

            for l in lines.split("\n"):
                list_line.append(l)

                if is_show_console:
                    print(l)

        print("The data as TXT have been gotten from PATH: {}".format(txt_path))
        return list_line


class UtilitiesAudioEditing():

    @staticmethod
    def cut_output_stream(video_path, index, start, end, save_path):

        stream = ffmpeg.input(video_path, ss=start, to=end)
        stream = ffmpeg.output(stream, save_path + "{}.mp3".format(str(index)))
        ffmpeg.run(stream, overwrite_output=True)
        print("The mp3 file is saved at {}".format(save_path + "{}.mp3".format(str(index))))

