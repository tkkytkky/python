#-*- coding: utf-8 -*-

#二分探索
#第一引数：探索対象のリスト
#第二引数：探索のキー値
#戻り値：見つかったときはTrueを返す
#		見つからないときはFalseを返す。
def binary_search(lst,key):
	#リストをソートする(Pythonのソートを利用
	lst.sort()

	#左端と右端のインデックスを取得
	left=0
	right=len(lst)-1

	#左右から半分ずつ絞っていく
	#最初に見つかった位置のインデックスを返すため、
	#左側を優先して探索する
	while left<right:
		middle=int((left+right)/2)
		if lst[middle]<key:
			#中央の値より探索の値が大きいときは
			#左側を中央の隣まで絞る
			left=middle+1
		else:
			#中央の値より探索の値が小さいか等しいときは
			#右側を中央まで絞る
			right=middle

		#左側と一致したときインデックスを返す
		if lst[left]==key:
			return True

	return False

#このプログラムを直接実行っしたときだけ以下の内容を実行する
if __name__=='__main__':
	lst=input("探索リストをスペース区切りで入力:")
	key=input("探索対象のキーを入力:")
	if binary_search(lst.split(),key):
		print("Contain value:",key)
	else:
		print("Not found:",key)