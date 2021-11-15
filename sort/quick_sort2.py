#-*- coding: utf-8 -*-

import random

#クイックソート（再帰無し）
#第一引数：ソート対象のリスト
#戻り値：ソートしたリスト
def quick_sort(a):
	n=len(a)

	#左右のインデックス位置をスタックとして保存
	indexstack=[(0,n-1)]
	right=left=0

	while len(indexstack)!=0:
		#左右の区間が1未満の場合はスタックから取得
		if right-left<1:
			#左右のインデックス血を取得
			left,right=indexstack.pop()

		#pivotを選択
		#random.choice()はランダムに要素を1つかｓ
		pivot=random.choice(a[left:right])

		#途中経過の表示
		#print(pivot,left,right,a)

		#pivotの前後の値を入れ替える
		i=left
		j=right
		while True:
			#前半でpivotより大きな値のインデックスを見つける
			while a[i]<pivot:
				i+=1

			#後半でpivotよりちいさな値のインデックスを見つける
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

		#スタック領域を少なくするために
		#広い区間をスタックに積んで短い区間を先に処理する
		if i-left>right-j:
			#左側のインデックスのpivotが先頭の直前になるまで続ける
			if i-1>left:
				indexstack.append((left,i-1))
			left=j+1
		else:
			#右側のインデックスのpivotが末尾の直前になるまで続ける
			if j+1<right:
				indexstack.append((j+1,right))
			right=i-1

	return a

#このプログラムを直接実行したときだけ以下の内容を実行
if __name__=='__main__':
	i=input("ソートしたい値をスペース区切りで入力：")
	print(quick_sort(i.split()))