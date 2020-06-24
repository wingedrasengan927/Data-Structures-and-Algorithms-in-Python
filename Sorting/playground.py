def partition(arr, start_index, end_index):
	pivot = arr[end_index]
	partition_index = start_index
	while start_index < end_index:
		if arr[start_index] <= pivot:
			arr[start_index], arr[partition_index] = arr[partition_index], arr[start_index]
			partition_index += 1
		start_index += 1
	arr[partition_index], arr[end_index] = arr[end_index], arr[partition_index]
	return partition_index

def quick_sort_helper(arr, start_index, end_index):
	if start_index >= end_index:
		return None
	partition_index = partition(arr, start_index, end_index)
	left_subarray = partition(arr, start_index, partition_index-1)
	right_subarray = partition(arr, partition_index+1, end_index)
	return arr

def quick_sort(arr):
	start_index = 0
	end_index = len(arr)-1
	return quick_sort_helper(arr, start_index, end_index)
	
arr = [12, 3, 4, 65, 7, 8, 90, 123, 23]
print(quick_sort(arr))