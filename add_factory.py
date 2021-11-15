#-*- ciding:utf-8 -*-

#作成したユークリッド互除法を読み込む
import euclidean

#最小公倍数
#第一引数：正の整数a
#第二引数：正の整数b
#戻り値：最小公倍数（整数）
def lcm(a,b):
	#ここに最小公倍数を返すプログラムを記述
	LCM=(a*b)/euclidean.gcd(a,b)
	return LCM


#直接実行された場合のみ実行
if __name__=='__main__':
	#値の入力
	print("LCM(a,b)")
	a=int(input("a="))
	b=int(input("b="))

	#最小公倍数を表示
	print(lcm(a,b))