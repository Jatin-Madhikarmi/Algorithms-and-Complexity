def MergeSort(arr):
    if(len(arr))<=1:
        return arr
    
    mid=len(arr)//2
    left_half=arr[:mid]
    right_half=arr[mid:]

    left_sorted=MergeSort(left_half)
    right_sorted=MergeSort(right_half)

    return Merge(left_sorted,right_sorted)

def Merge(left,right):
    sorted_arr=[]
    i=j=0

    while i <len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i+=1
        else:
            sorted_arr.append(right[j])
            j+=1
    
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


if __name__ == "__main__":
    unsorted_list = [38, 27, 43, 3, 9, 82, 10]
    print(f"Unsorted array: {unsorted_list}")
    
    sorted_list = MergeSort(unsorted_list)
    print(f"Sorted array:   {sorted_list}")
