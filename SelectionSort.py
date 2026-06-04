def SelectionSort(arr):
    n=len(arr)

    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx=j
        # Swap the values
        # Pythonic way to do it
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

arr=[5,3,7,8,9,1,2,6,7]
sortedArray=SelectionSort(arr)
print(f"The sorted lis is {sortedArray}")