import copy


def txt_format(input_txt, str_thresh):
    new_text = ""
    format_list = []
    text_file_list = []
    str_num = 0
    print("テキストファイルの改行修正中・・・")
    # 文字列の結合
    mojiretu_num = len(input_txt)

    # 抽出した文字列内に「.」や「。」のチェック
    for i in range(mojiretu_num):
        # .(ピリオド)がきたら区切る
        if input_txt[i] == ".":
            if i < mojiretu_num - 3:
                new_text += "."
                # 先頭と末尾の半角スペースを削除
                tmp = new_text.strip()
                format_list.append(tmp)
                new_text = ""
        # それ以外は通常記入
        else:
            new_text += input_txt[i]
        # 文字数チェック
        for i in format_list:
            str_num += len(i)
        # 文字数が閾値超えたら新しいファイルを作成
        if str_num > str_thresh:
            print("文字数が{}文字を超えました。ファイルを追加します。".format(str_thresh))
            text_file_list.append(copy.deepcopy(format_list))
            format_list.clear()
        str_num = 0

    return text_file_list, format_list
