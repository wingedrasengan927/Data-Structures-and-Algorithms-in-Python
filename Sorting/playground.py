def insertion_sort(arr):
	if len(arr) == 1:
		return arr
	for i in range(1, len(arr)):
		current_index = i
		for j in reversed(range(i)):
			if arr[current_index] < arr[j]:
				arr[current_index], arr[j] = arr[j], arr[current_index]
				current_index = j
	return arr

arr = [1, 5, 2, 3, 8, 7, 12]
print(insertion_sort(arr))