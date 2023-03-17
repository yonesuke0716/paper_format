from googletrans import Translator


def english_to_japanese(text_file_list, format_list):
    f_num = 0
    print("修正したテキストを翻訳中・・・")
    translator = Translator()
    # str_thresh文字以上超えた出力
    if len(text_file_list) > 0:
        for t_file in text_file_list:
            f_num += 1
            with open("output_{}.txt".format(f_num), mode="w", encoding="utf-8") as f:
                for t_1 in t_file:
                    translated = translator.translate(t_1, dest="ja")
                    print(t_1, file=f)
                    print(translated.text, file=f)  # 翻訳後の文章

    # str_thresh文字以内の出力
    f_num += 1
    with open("output_{}.txt".format(f_num), mode="w", encoding="utf-8") as f:
        for t_2 in format_list:
            translated = translator.translate(t_2, dest="ja")
            print(t_2, file=f)
            print(translated.text, file=f)  # 翻訳後の文章
