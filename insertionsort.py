def insertion_sort(arr):
    # Traverse from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Place the key in its correct sorted position
        arr[j + 1] = key

# Example usage:
if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]
    insertion_sort(data)
    print("Sorted array:", data)
