def Insertionsort(arr):
    n=len(arr)

    for i in range(1,n):
        key=arr[i]
        j=i-1

        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

    return arr

arr=[4,5,6,1,2,54,67,11,9]
print(f"The unsorted list is {arr}")
print(f"The sorted list is {Insertionsort(arr)}")
