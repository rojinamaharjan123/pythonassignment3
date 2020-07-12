
def partition(arr, start, end):
    pivot = start
    for i in range(start+1, end+1):
        if arr[i] <= arr[start]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]
    arr[pivot], arr[start] = arr[start], arr[pivot]
    return pivot



def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    def _quicksort(arr, start, end):
        if start >= end:
            return
        pivot = partition(arr, start, end)
        _quicksort(arr, start, pivot-1)
        _quicksort(arr, pivot+1, end)
    return _quicksort(arr, start, end)

print("The sorted list through quick sort is:")
unsorted_list=[34,56,78,54,33,24,98,76]
quick_sort(unsorted_list)
print(unsorted_list)