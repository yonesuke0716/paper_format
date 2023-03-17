import copy


def txt_format(file_path, str_thresh):
    new_text = ""
    format_list = []
    text_file_list = []
    str_num = 0
    print("テキストファイルの改行修正中・・・")
    # テキストファイル内の文字列の読み込み
    with open(file_path, encoding="utf-8") as f:
        l_strip = [s.strip() for s in f.readlines()]

    # 文字列の結合
    mojiretu = " ".join(l_strip)

    mojiretu_num = len(mojiretu)

    # 抽出した文字列内に「.」や「。」のチェック
    for i in range(mojiretu_num):
        if mojiretu[i] == ".":
            if i < mojiretu_num - 3:
                # .comは除く
                if (
                    mojiretu[i + 1] == "c"
                    and mojiretu[i + 2] == "o"
                    and mojiretu[i + 3] == "m"
                ):
                    new_text += mojiretu[i]
                # .comじゃなければ改行
                else:
                    new_text += "."
                    # 先頭と末尾の半角スペースを削除
                    tmp = new_text.strip()
                    format_list.append(tmp)
                    new_text = ""
            else:
                new_text += "."
                # 先頭と末尾の半角スペースを削除
                tmp = new_text.strip()
                format_list.append(tmp)
                new_text = ""
        elif mojiretu[i] == "。":
            new_text += "。"
            # 先頭と末尾の半角スペースを削除
            tmp = new_text.strip()
            format_list.append(tmp)
            new_text = ""
        else:
            new_text += mojiretu[i]
        # 文字数チェック
        for i in format_list:
            str_num += len(i)

        if str_num > str_thresh:
            print("文字数が{}文字を超えました。ファイルを追加します。".format(str_thresh))
            text_file_list.append(copy.deepcopy(format_list))
            format_list.clear()
        str_num = 0

    return text_file_list, format_list
