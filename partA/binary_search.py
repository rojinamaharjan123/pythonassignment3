sorted_list=[4,5,6,7,8,9,20,11]
item=int(input("Enter the item that you want to find"))

def binary_search(arr,l,r,f):
    mid=l+r/2
    if  f==mid:
        return ("Item found")
    elif f>mid:
        return binary_search(arr,mid+1,r,f)
    elif f<mid:
        return binary_search(arr,l,mid-1,f)
    else:
        return ("Item not found")

binary_search(sorted_list,0,7,item)

    