# -*- coding: utf-8 -*-

# ユークリッドの互除法で最大公約数を求める
# 第1引数 : 正の整数a
# 第2引数 : 正の整数b
def gcd(a, b):
    # a が b より小さいときは a と b を入れ替える
    if a < b:
        a, b = b, a

    # b が 0 になるまで繰り返す
    while b != 0:
        # a を b で割った余りrを求め, a = b, b = r とする
        r = a % b
        a, b = b, r

    # a が最大公約数
    return a

# 再帰を利用して最大公約数を求める
# 第1引数 : 正の整数a
# 第2引数 : 正の整数b
def rgcd(a, b):
    # a が b より小さいときは a と b を入れ替える
    if a < b:
        a, b = b, a

    # b が 0 であれば a が最大公約数
    if b == 0:
        return a

    # b と (a を b で割った余り) の最大公約数を求める
    return rgcd(b, a % b)

# 直接実行された場合のみ実行
if __name__ == '__main__':
    # 値の入力
    print("gcd(a, b)")
    a = int(input("a = "))
    b = int(input("b = "))

    # ユークリッドの互除法
    print("ユークリッドの互除法")
    print(gcd(a, b))

    # 再帰版
    print("再帰版")
    print(rgcd(a, b))

    # 数学関数モジュール版
    print("Python数学関数モジュール版")
    import math
    print(math.gcd(a, b))

