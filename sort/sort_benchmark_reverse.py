#-*- coding: utf-8 -*-

#Benchmarker を使う時はWindows PowerShellから
#「pip install Benchmarker」を実行してパッケージを導入しておく
#注) １度導入してけば良い

from benchmarker import Benchmarker
import random
import bubble_sort
import selection_sort
import insertion_sort
import heap_sort
import merge_sort
import quick_sort1
import quick_sort2
import python_sort

#繰り返しの数を文字列から整数に直して取得
n=int(input("ソートする値のサイズ="))

#サイズのリストを生成
array=list(range(0,n))

#リストの中身を逆順にしておく
array.reverse()

#arrayをコピーしておく
#数値のみなので浅いコピーで良い
array1=array.copy()
array2=array.copy()
array3=array.copy()
array4=array.copy()
array5=array.copy()
array6=array.copy()
array7=array.copy()

#ソートのベンチマーク
with Benchmarker(n,width=32) as bench:
	@bench("bubble_sort")
	def _(bm):
		bubble_sort.bubble_sort(array1)

	@bench("selection_sort")
	def _(bm):
		selection_sort.selection_sort(array2)

	@bench("insertion_sort")
	def _(bm):
		insertion_sort.insertion_sort(array3)

	@bench("heap_sort")
	def _(bm):
		heap_sort.heap_sort(array4)

	@bench("merge_sort")
	def _(bm):
		merge_sort.merge_sort(array5)

	@bench("quick_sort1(recursive)")
	def _(bm):
		quick_sort1.quick_sort(array6)

	@bench("quick_sort2(not recursive")
	def _(bm):
		quick_sort2.quick_sort(array7)



		
