def shell_sort(array):
    n = len(array)
    gap = n // 2

    # Start with a big gap, then reduce the gap
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            # Shift earlier gap-sorted elements until the correct location for array[i] is found
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            # Put temp (the original array[i]) in its correct location
            array[j] = temp
        gap //= 2

# Get list of numbers from the user
user_input = input("Enter numbers separated by space: ")
array = list(map(int, user_input.split()))

# Perform shell sort
shell_sort(array)

# Print the sorted array
print("Sorted array:", array)
