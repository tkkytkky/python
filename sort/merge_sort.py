#-*- coding: utf-8 -*-

import math

#マージソートの再帰部分
#第一引数：ソート対象のリスト
#第二引数：マージ先頭インデックス
#第三引数：マージ末尾インデックス
#第四引数：作業用リスト
#戻り値：ソートしたリスト
def _merge_sort_recursion(a,first,last,work):
	#先頭と末尾が一つになるまで実行
	if first<last:
		#データ列を前半と後半に分割してそれぞれを再帰的に処理
		middle=int((first+last)/2)
		_merge_sort_recursion(a,first,middle,work)
		_merge_sort_recursion(a,middle+1,last,work)

		#途中経過の表示
		#print(first,last,a)

		#前半部分を作業用リストwork移す
		wk_size=0
		for i in range(first,middle+1):
			work[wk_size]=a[i]
			wk_size+=1

		#前半部分と後半部分をマージする
		i=0
		j=middle+1
		k=first
		while i<wk_size and j<=last:
			#前半と後半を比較
			if work[i]<=a[j]:
				#前半が小さければ
				#作業用リストに入れた前半の値を上書き
				a[k]=work[i]
				k+=1
				i+=1
			else:
				#後半が小さければ後半の値を上書き
				a[k]=a[j]
				k+=1
				j+=1

		#この時点で前半または後半に
		#マージしていない部分は残っている

		#前半部分の残りだけを書き戻す
		#残った後半部分はリストaの公判でソートされた状態なので
		#戻す必要がない
		while i<wk_size:
			a[k]=work[i]
			k+=1
			i+=1
	return a

#マージソート
#第一引数：ソート対象のリスト
#戻り値：ソートしたリスト
def merge_sort(lst):
	n=len(lst)

	#作業用リストの生成
	#リストの半分のサイズ(切り上げ)を初期化する
	work=[0]*(math.ceil(n/2))

	#配列全体をマージソートの対象とする
	lst=_merge_sort_recursion(lst,0,n-1,work)

	return lst

#このプログラムを直接実行したときだけ以下の内容を実行する
if __name__=='__main__':
	i=input("ソートしたい値をスペース区切りで入力:")
	print(merge_sort(i.split()))