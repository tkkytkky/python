# -*- coding: utf-8 -*-

# Python標準のソート(ティムソート)
# 第1引数 : ソート対象のリスト
# 戻り値 : ソートしたリスト
def python_sort(lst):
    lst.sort()
    return lst

# このプログラム直接実行したときだけ以下の内容を実行する
if __name__ == '__main__':
    i = input("ソートしたい値をスペース区切りで入力 : ")
    print(python_sort(i.split()))
