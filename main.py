import copy
import configparser
from googletrans import Translator

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8-sig')

file_path  = config_ini['data']['file_path']

# global
str_thresh = int(config_ini['data']['str_thresh'])


def main():
    new_text = ''
    new_list = []
    text_file_list = []
    str_num = 0
    f_num = 0
    print("テキストファイルの改行修正中・・・")
    # テキストファイル内の文字列の読み込み
    with open(file_path, encoding="utf-8") as f:
        l_strip = [s.strip() for s in f.readlines()]

    # 文字列の結合
    mojiretu = ' '.join(l_strip)

    mojiretu_num = len(mojiretu)

    # 抽出した文字列内に「.」や「。」のチェック
    for i in range(mojiretu_num):
        if mojiretu[i] == '.':
            if i < mojiretu_num - 3:
                # .comは除く
                if mojiretu[i+1] == 'c' and mojiretu[i+2] == 'o' and mojiretu[i+3] == 'm':
                    new_text += mojiretu[i]
                # .comじゃなければ改行
                else:
                    new_text += "."
                    # 先頭と末尾の半角スペースを削除
                    tmp = new_text.strip()
                    new_list.append(tmp)
                    new_text = ''
            else:
                new_text += "."
                # 先頭と末尾の半角スペースを削除
                tmp = new_text.strip()
                new_list.append(tmp)
                new_text = ''
        elif mojiretu[i] == '。':
            new_text += "。"
            # 先頭と末尾の半角スペースを削除
            tmp = new_text.strip()
            new_list.append(tmp)
            new_text = ''
        else:
            new_text += mojiretu[i]
        # 文字数チェック
        for i in new_list:
            str_num += len(i)

        if str_num > str_thresh:
            print("文字数が{}文字を超えました。ファイルを追加します。".format(str_thresh))
            text_file_list.append(copy.deepcopy(new_list))
            new_list.clear()
        str_num = 0

    print("修正したテキストを翻訳中・・・")
    translator = Translator()
    # str_thresh文字以上超えた出力
    if len(text_file_list) > 0:
        for t_file in text_file_list:
            f_num += 1
            with open('output_{}.txt'.format(f_num), mode='w', encoding="utf-8") as f:
                for t_1 in t_file:
                    translated = translator.translate(t_1, dest="ja")
                    print(t_1, file=f)
                    print(translated.text, file=f)  # 翻訳後の文章

    # str_thresh文字以内の出力
    f_num += 1
    with open('output_{}.txt'.format(f_num), mode='w', encoding="utf-8") as f:
        for t_2 in new_list:
            translated = translator.translate(t_2, dest="ja")
            print(t_2, file=f)
            print(translated.text, file=f)  # 翻訳後の文章


if __name__ == '__main__':
    main()
    print("翻訳が完了しました。")