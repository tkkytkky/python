#-*- coding: utf-8 -*-

import random

#クイックソートの再帰部分
#第一引数：ソート対象のリスト
#第二引数：先頭インデックス
#第三引数：末尾インデックス
#戻り値：ソートしたリスト
def _quick_sort_recursion(a,first,last):
	#pivotを選択
	#random.choice()はランダムに要素を1つ返す
	pivot=random.choice(a[first:last])

	#途中経過の表示
	#print(pivot,first,last,a)

	#pivotの前後の値を入れ替える
	i=first
	j=last
	while True:
		#前半でpivotより大きな値のインデックスを見つける
		while a[i]<pivot:
			i+=1

		#後半でpivotより小さな値のインデックスを見つける
		while a[j]>pivot:
			j-=1

		#pivotの前後のインデックスが逆転した場合は終了
		if i>=j:
			break;

		#pivotの前後で大きい値と小さい値を入れ替える
		a[i],a[j]=a[j],a[i]

		#次のインデックスに進める
		i+=1
		j-=1

	#右側のインデクス鵜のpivotが末尾の直前になるまで続ける
	if j+1<last:
		_quick_sort_recursion(a,j+1,last)

	#左側のインデックスのpivotが先頭の直前になるまで続ける
	if i-1>first:
		_quick_sort_recursion(a,first,i-1)

	return a

#クイックソート（再帰を利用）
#第一引数：ソート対象のリスト
#戻り値：ソートしたリスト
def quick_sort(lst):
	n=len(lst)

	#配列全相をクイックソートの対象とする
	lst=_quick_sort_recursion(lst,0,n-1)

	return lst

#このプログラムを直絶時こうしたときだけ以下の内容を実行
if __name__=='__main__':
	i=input("ソートしたい値をスペース区切りで入力：")
	print(quick_sort(i.split()))