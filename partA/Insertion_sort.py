unsorted_list=[4,6,7,8,2,4,5,9]


def Insertion_sort(arr):
    count=len(arr)
    for i in range(1,count):
        temp=arr[i]
        j=i-1
        while j>=0 and  temp<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=temp


print("The sorted list using insertion sort is:")
Insertion_sort(unsorted_list)
print(unsorted_list)