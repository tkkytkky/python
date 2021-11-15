﻿##-*- coding: utf-8 -*-

#ヒープの再構築
#第一引数：ソート対象のリスト
#第二引数：ソート対象の要素数
#第三引数：構築対象の要素a[i]のインデックス
#第四引数：構築対象となる要素の値
def _heap_rebuild(a,n,i,x):
	#左の子のインデックスを計算
	j=2*i
	while j<=n:
		#左右の子で右の子が大きいときは
		#右の子のインデックス（＋１）にする
		if j<n and a[j]<a[j+1]:
			j+=1
		#子が小さい場合は終了
		if x>=a[j]:
			break
		#子が大きいので親に代入
		a[i]=a[j]
		#子を親とする
		i=j
		#自分の左の子のインデックスを計算
		j=2*i
	
	#対象の値をノードに代入
	a[i]=x
	return a

#ヒープソート
#第一引数：トート対象のリスト
#戻り値：ソートしたリスト
def heap_sort(a):
	#要素数を取得
	n=len(a)

	#要素の先頭に一時的な値を挿入して1~nの値をソートする
	a.insert(0,0)

	#ヒープを構築する
	#最下層の右端にあり親子から再構築する
	for i in range(int(n/2),0,-1):
		#i番目を再構築
		x=a[i]
		a=_heap_rebuild(a,n,i,x)

		#途中経過のヒープを表示
		#print(a)

	#根の最大値を取り出して最下層右端に代入し
	#最下層の右端はソート済みとして再構築を繰り返す
	for i in range(n,1,-1):
		#最下層右端の要素の値を取りだして
		#最大値を最下層の右端の要素に代入する
		x=a[i]
		a[i]=a[1]

		#最下層の右端はソート済みとしてi-1とし
		#最下層の右端の値を挿入して再構築
		a=_heap_rebuild(a,i-1,1,x)

		#途中経過の表示
		#print(i,a)

	#要素の先頭の一時的な値を削除する
	del a[0]
	return a


#このプログラムを直接実行したときだけ以下の内容を実行
if __name__=='__main__':
	i=input("ソートしたい値をスペース区切りで入力:")
	print(heap_sort(i.split()))