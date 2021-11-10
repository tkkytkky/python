#-*- coding: utf-8 -*-
import sys

change=input("お釣りを入力して下さい:")
if not change.isdigit():
	print("お釣りは整数で入力して下さい。")
	sys.exit()

#お釣りを整数に変換
change=int(change)

#500円球を求める
yen500=change//500
if yen500>0:
	change=change%500

#100円玉を求める
yen100=change//100
if yen100>0:
	change=change%100

#50円玉を求める
yen50=change//50
if yen50>0:
	change=change%50

#10円玉を求める
yen10=change//10
if yen10>0:
	change=change%10

#5円玉を求める
yen5=change//5
if yen5>0:
	change=change%5

#求めた硬貨を表示
print("500円玉:{0}枚".format(yen500))
print("100円玉:{0}枚".format(yen100))
print("50円玉: {0}枚".format(yen50))
print("10円玉: {0}枚".format(yen10))
print("5円玉:  {0}枚".format(yen5))
print("1円玉:  {0}枚".format(change))