def find_thesmallest(arr):
    smallest = arr[0] # The smallest amount.
    smallest_index = 0 # The index of the smallest amount.
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_thesmallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

print(selection_sort([5, 3, 6, 2, 10]))