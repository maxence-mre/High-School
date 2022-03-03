from argparse import ArgumentParser
from os.path import isfile, isdir
from pickle import load, dump
from random import randint
from time import time
from os import mkdir

import sys

def GetExecutionTime(function, liste, prnt=False):
	start = time()
	liste = function(liste)
	if liste != sorted(liste):
		return False
	end = time()
	if prnt:
		[print(e) for e in liste]
		print()
	return abs(end-start)

def Median(liste):
	if len(liste) == 0:
		return 0
	total = 0
	for ele in liste:
		total += ele
	return total / len(liste)


############ MERGE SORT ############

def merge(left, right):
	if left == None:
		return right
	if right == None:
		return left
	if len(left) == 0:
		return right
	if len(right) == 0:
		return left
	result = []
	index_left = index_right = 0
	while len(result) < len(left) + len(right):
		if left[index_left] <= right[index_right]:
			result.append(left[index_left])
			index_left += 1
		else:
			result.append(right[index_right])
			index_right += 1
		if index_right == len(right):
			result += left[index_left:]
			break
		if index_left == len(left):
			result += right[index_right:]
			break
	return result

def merge_sort(array):
	if len(array) < 2:
		return array

	midpoint = len(array) // 2

	return merge(left=merge_sort(array[:midpoint]), right=merge_sort(array[midpoint:]))

############ TIMSORT ############

def timsort_insert(array, left=0, right=None):
	if right is None:
		right = len(array) - 1

	copied = array[:]
	for i in range(left + 1, right + 1):
		key_item = copied[i]
		j = i - 1
		while j >= left and copied[j] > key_item:
			copied[j + 1] = copied[j]
			j -= 1
		copied[j + 1] = key_item
	return copied

def timsort(array):
	copied = array[:]

	min_run = 32
	n = len(array)
	for i in range(0, n, min_run):
		copied = timsort_insert(copied, i, min((i + min_run - 1), n - 1))

	size = min_run
	while size < n:
		for start in range(0, n, size * 2):
			midpoint = start + size - 1
			end = min((start + size * 2 - 1), (n-1))
			merged_array = merge(
				left=array[start:midpoint + 1],
				right=array[midpoint + 1:end + 1])
			copied[start:start + len(merged_array)] = merged_array
		size *= 2
	return copied

############ BUBBLE SORT ############

def bubble_sort(arr):
	copied = arr[:]

	n = len(copied)
	for i in range(n-1):
		for j in range(0, n-i-1):
			if copied[j] > copied[j + 1] :
				copied[j], copied[j + 1] = copied[j + 1], copied[j]
	return copied

############ CHEAT ############

def cheatSort(arr):
	return sorted(arr)

############ INSERTION SORT ############

def insertionSort(arr):
	copied = arr[:]

	for i in range(1, len(copied)):
		key = copied[i]
		j = i-1
		while j >= 0 and key < copied[j] :
			copied[j + 1] = copied[j]
			j -= 1
		copied[j + 1] = key
	return copied


############ QUICKSORT ############

def part(arr, low, high):
	i = (low-1)
	pivot = arr[high]

	for j in range(low, high):
		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)


def sortQuick(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:
		pi = part(arr, low, high)
		sortQuick(arr, low, pi-1)
		sortQuick(arr, pi+1, high)

def quickSort(arr):
	copied = arr[:]
	sortQuick(copied, 0, len(arr)-1)
	return copied


############ END ############


SORT_ALGORITHMS = {
	"Merge sort"     : merge_sort,
	"Timesort"       : timsort,
	"Bubble sort"    : bubble_sort,
	#"Cheat sort"     : cheatSort,
	"Insertion sort" : insertionSort,
	"Quicksort"      : quickSort
}

def GenerateListe(args):
	liste = []
	if args.file != None:
		try:
			liste = load(open(args.file, "rb"))
		except:
			liste = []
			with open(args.file, "r") as r:
				for e in r.read().split("\n"):
					try:
						liste.append(int(e))
					except:
						raise ValueError("File you pass as argument must have one integer by line")
	else:
		for _ in range(randint(args.min_length, args.max_length)):
			liste.append(randint(args.min_value, args.max_value))
	return liste



def main():
	parser = ArgumentParser(description="Python Sorted, program used to sort a list as quickly as possible")
	parser.add_argument("-f", "--feed",
	dest="feed",
	action="store_true",
	default=False,
	help="Feed AI datas")

	parser.add_argument("-p", "--print",
	dest="print",
	action="store_true",
	default=False,
	help="Print the sorted list")

	parser.add_argument("-n", "--number",
	dest="number",
	metavar="number",
	type=int, nargs="?",
	default=1,
	help="Sort multiple times")

	parser.add_argument("-l", "--list-file",
	dest="file",
	metavar="file",
	type=open, nargs="?",
	default=None,
	help="File where list is stored. Pickle list, or one element by line"
	)

	parser.add_argument("-mil", "--min-length",
	dest="min_length",
	metavar="min_length",
	type=int, nargs="?",
	default=10,
	help="Minimum value of length of array")

	parser.add_argument("-mal", "--max-length",
	dest="max_length",
	metavar="max_length",
	type=int, nargs="?",
	default=20,
	help="Maximum value of length of array")

	parser.add_argument("-miv", "--min-value",
	dest="min_value",
	metavar="min_value",
	type=int, nargs="?",
	default=0,
	help="Minimum value of array")

	parser.add_argument("-mav", "--max-value",
	dest="max_value",
	metavar="max_value",
	type=int, nargs="?",
	default=100,
	help="Maximum value of array")

	args = parser.parse_args()

	sys.setrecursionlimit(args.max_length**2)

	if not isdir("aidata/"):
		mkdir("aidata/")
	if not isfile("aidata/aidata.pkl"):
		data = {}
	else:
		data = load(open("aidata/aidata.pkl", "rb"))
	
	for _ in range(args.number):
		liste = GenerateListe(args)
	
		if args.feed:
			header = (len(data), len(liste), Median(liste), min(liste), max(liste))
			data[header] = {}
			for a, b in SORT_ALGORITHMS.items():
				tp = GetExecutionTime(b, liste, args.print)
				if not tp:
					print(f"Algorithm \"{a}\" just had errors and did not return sorted array !")
					continue
				print(f"Algorithm \"{a}\" made it on {tp} seconds !")
				data[header][a] = tp
			dump(data, open("aidata/aidata.pkl", "wb+"))
			print("Saved executions infos !")
		else:
			if len(list(data.keys())) == 0:
				raise ValueError("Please feed the AI before using !!!")

			headers = list(data.keys())

			best = {headers[0][0]: -1}
			for h in headers:
				h_id, h_length, h_median, h_min, h_max = h
				l_length, l_median, l_min, l_max = len(liste), Median(liste), min(liste), max(liste)

				dif = abs(h_length - l_length) + abs(h_median - l_median) + abs(h_min - l_min) + abs(h_max - l_max)
				if list(best.values())[0] == -1 or list(best.values())[0] > dif:
					best = {h_id : dif}

			header = headers[list(best.keys())[0]]

			actual = data[header]
			best = list(actual.keys())[0]
			for a, b in actual.items():
				if b < actual[best]:
					best = a

			tp = GetExecutionTime(SORT_ALGORITHMS[best], liste, args.print)
			print(f"Using algorithm \"{best}\", total time is : {tp}")


if __name__ == "__main__":
	main()
