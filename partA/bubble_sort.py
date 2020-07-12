unsorted_list=[78,45,34,23,13,6,89,54,43]


def bubble_sort(l):
    count=len(l)
    for i in range(count):
        for j in range(0,count-i-1):
            if(l[j]>l[j+1]):
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp

print("the sorted list is :")
bubble_sort(unsorted_list)
print(unsorted_list)