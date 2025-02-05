def bubble_sort(arr):
    """
    This function sorts a list (array) using the Bubble Sort algorithm.
    Bubble Sort repeatedly swaps adjacent elements if they are in the wrong order.
    """

    n = len(arr)  # Get the number of elements in the list

    # Outer loop: Iterate through the list 'n' times
    for i in range(n):

        # Inner loop: Compare adjacent elements and swap if needed
        # The last 'i' elements are already sorted in each iteration, so we reduce the range
        for j in range(0, n - i - 1):

            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr  # Return the sorted list

# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)  # Output: [11, 12, 22, 25, 34, 64, 90]
