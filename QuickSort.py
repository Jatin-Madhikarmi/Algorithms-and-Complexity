def QuickSort(arr,low,high):
    # We recursively run the loop only when the low is less tha high
    if low < high:
        #* pi refers to the partition index i.e this index will be in it's correct position in the final sorted array*#
        pi=partition(arr,low,high)

        QuickSort(arr,low,pi-1)
        QuickSort(arr,pi+1,high)


def partition(arr,low,high):
    pivot=arr[high] # The pivot element is set to the last element of our list
    i=low-1 # Here the value of i is always 1 less than j
    for j in range(low,high):
        if arr[j] <= pivot: 
            i+=1 # Only when the value of array given by the index j is less than the pivot we increment the value of i 
            # It is done becuase the value that will contain in i will always be greater or equal to the value in j so we swap them
            # Swap the values between i and j
            arr[i],arr[j]=arr[j],arr[i]
    # Now we swap the pivot elements
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

# Example usage:
data = [10, 7, 8, 9, 1, 5]
QuickSort(data, 0, len(data) - 1)
print("Sorted array:", data)
# Output: [1, 5, 7, 8, 9, 10]