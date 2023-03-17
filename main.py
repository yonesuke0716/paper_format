import configparser

import txt_format
import translate

# import read_pdf
# import gpt3_summary


config_ini = configparser.ConfigParser()
config_ini.read("config.ini", encoding="utf-8-sig")

file_path = config_ini["data"]["file_path"]

# global
str_thresh = int(config_ini["data"]["str_thresh"])


def main():
    # テキストファイルの整形
    text_file_list, format_list = txt_format.txt_format(file_path, str_thresh)
    # 英語→日本語
    translate.english_to_japanese(text_file_list, format_list)


if __name__ == "__main__":
    main()
    print("翻訳が完了しました。")
