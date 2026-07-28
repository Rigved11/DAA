def linear_search(arr, target):
    # Loop through every element and its index
    for index, element in enumerate(arr):
        # Return the index if the target matches
        if element == target:
            return index
            
    # Return -1 if the target is not in the list
    return -1

# Example usage:
if __name__ == "__main__":
    data = [10, 23, 45, 70, 11, 15]
    target_value = 70
    
    result = linear_search(data, target_value)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the list.")
