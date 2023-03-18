import configparser

import txt_format
import translate
import read_pdf

# import gpt3_summary


config_ini = configparser.ConfigParser()
config_ini.read("config.ini", encoding="utf-8-sig")

file_path = config_ini["data"]["file_path"]

# global
str_thresh = int(config_ini["data"]["str_thresh"])


def main():
    # pdfファイル指定時
    if file_path.endswith("pdf"):
        out_txt = read_pdf.pdf_to_txt(file_path)
    # txtファイル指定時
    elif file_path.endswith("txt"):
        with open(file_path, encoding="utf-8") as f:
            l_strip = [s.strip() for s in f.readlines()]
        out_txt = " ".join(l_strip)
    # テキストファイルの整形
    text_file_list, format_list = txt_format.txt_format(out_txt, str_thresh)
    # 英語→日本語
    translate.english_to_japanese(text_file_list, format_list)


if __name__ == "__main__":
    main()
    print("翻訳が完了しました。")
