import os
from tqdm import tqdm
from googletrans import Translator


def english_to_japanese(text_file_list, format_list):
    f_num = 0
    os.makedirs("output", exist_ok=True)
    print("修正したテキストを翻訳中・・・")
    translator = Translator()
    # str_thresh文字以上超えた出力
    if len(text_file_list) > 0:
        for text_file in text_file_list:
            f_num += 1
            with open(
                "output/output_{}.txt".format(f_num), mode="w", encoding="utf-8"
            ) as f:
                for t_num in tqdm(range(len(text_file))):
                    translated = translator.translate(text_file[t_num], dest="ja")
                    print(text_file[t_num], file=f)
                    print(translated.text, file=f)  # 翻訳後の文章

    # str_thresh文字以内の出力
    f_num += 1
    with open("output/output_{}.txt".format(f_num), mode="w", encoding="utf-8") as f:
        for f_num in tqdm(range(len(format_list))):
            translated = translator.translate(format_list[f_num], dest="ja")
            print(format_list[f_num], file=f)
            print(translated.text, file=f)  # 翻訳後の文章
