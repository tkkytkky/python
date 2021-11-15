#-*- coding: utf-8 -*-

#バブルソート
#第一引数：ソート対象のリスト
#戻り値：ソートしたリスト
def bubble_sort(lst):
	n=len(lst)
	for i in range(0,n-1):
		for j in range(n-1,i,-1):
			#前の値と比較
			if (lst[j-1]>lst[j]):
				#前の要素と交換
				lst[j-1],lst[j]=lst[j],lst[j-1]

		#途中経過の表示
		#print(i,lst)

	return lst

#このプログラムを直接実行したときだけ以下の内容を実行する
if __name__=='__main__':
	i=input("ソートしたい値をスペース区切り入力:")
	print(bubble_sort(i.split()))
