def heapify(arr, n, i):
    """
    To heapify a subtree rooted with node i which is an index in arr[].
    n is the size of the heap.
    """
    largest = i          # Initialize largest as root
    left = 2 * i + 1     # Left child index:  2i + 1
    right = 2 * i + 2    # Right child index: 2i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child of root exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Main function to sort an array of given size using Heap Sort.
    """
    n = len(arr)

    # Step 1: Build a max heap
    # Index of last non-leaf node is (n // 2) - 1
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        # Move current root (largest element) to the end of the array
        arr[i], arr[0] = arr[0], arr[i]
        
        # Call max heapify on the reduced heap
        heapify(arr, i, 0)


# --- Example Execution ---
if __name__ == "__main__":
    # Input unsorted array
    example_array = [12, 11, 13, 5, 6, 7]
    
    print("Original array: ")
    print(example_array)
    
    # Perform Heap Sort
    heap_sort(example_array)
    
    print("\nSorted array: ")
    print(example_array)