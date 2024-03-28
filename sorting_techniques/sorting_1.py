# Selection Sort Algorithm
# get the minimum and swap it to left index. then increment the left index by 1.
TC O(N^2) SC O(1)
def selection_sort(arr):
    for l in range(len(arr)-1):
        min_val = l
        swapped = False
        for r in range(l,len(arr)):
            if arr[r] < arr[min_val]:
                min_val = r
                swapped = True
        arr[min_val], arr[l]= arr[l], arr[min_val]
        if not swapped:
            break
    return arr
x = [7, 5, 9, 2, 8]
print('Before sorting',x)
print('After sorting',selection_sort(x))

# Bubble Sort Algorithm

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        swapped = False  # Initialize swapped flag
        # Last i elements are already in place, so we don't need to check them again
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True  # Set swapped flag to True if a swap is performed
        print(arr)
        # If no swap is performed in the inner loop, the array is already sorted
        # So, we can break the outer loop
        if not swapped:
            break
x = [2,13, 4, 1, 3, 6, 28]
print('Before sorting',x)
print('After sorting',bubble_sort(x))
