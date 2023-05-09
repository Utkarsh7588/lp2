def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Take input from user for array elements
arr = []
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    arr.append(int(input("Enter element {}:".format(i+1))))

# Call selection sort function
sorted_arr = selection_sort(arr)

# Print the sorted array
print("Sorted array:", sorted_arr)
