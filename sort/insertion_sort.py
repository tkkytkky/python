#-*- coding: utf-8 -*-

#挿入ソート
#第一引数：ソート対称のリスト
#戻り値：ソートしたリスト
def insertion_sort(lst):
	n=len(lst)

	#0番目の要素は操作済みとして1から始める
	for i in range(1,n):
		#未捜査の値を一時領域に保存する
		tmp=lst[i]

		#操作済みの値と比べて挿入対称となるまで入れ替える
		j=i-1
		while j>=0 and lst[j]>tmp:
			lst[j+1]=lst[j]
			j-=1

		#未捜査の値を挿入
		lst[j+1]=tmp

		#途中経過の表示
		#print(i,lst)

	return lst

#このプログラム直接実行したときだけ以下の内容を実行する
if __name__=='__main__':
	i=input("ソートしたい値をスペース区切りで入力:")
	print(insertion_sort(i.split()))