#-*- coding: utf-8 -*-

#選択ソート
#第一引数：ソート対象のリスト
#戻り値：ソートしたリスト
def selection_sort(lst):
	n=len(lst)
	for i in range(0,n-1):
		#交換対象のインデックス
		index=i
		for j in range(i+1,n):
			#最小値の要素と比較
			if (lst[j]>lst[index]):
				#最小値の要素のインデックスを保管
				index=j

		#最小値の要素と入れ替え
		lst[index],lst[i]=lst[i],lst[index]

		#途中経過の表示
		#print(i,lst)

	return lst

#このプログラムを直接実行したときだけ以下の内容を実行する
if __name__=='__main__':
	i=input("ソートしたい値をスペース区切り入力:")
	print(selection_sort(i.split()))
