# Selection Sort Algorithm
# get the minimum in range and swap it to left index. then increment the left index by 1.
# Time complexity: O(N2), (where N = size of the array), for the  worst and O(N) for the best case
# Space Complexity: O(1)
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
# take the highest element and place it in right most corner and repeat the same for each iteration
# Time Complexity: O(N2) for the worst and average cases and O(N) for the best case. Here, N = size of the array.
# Space Complexity: O(1)
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for l in range(n):
        swapped = False  # Initialize swapped flag
        # Last l elements are already in place, so we don't need to check them again
        for r in range(0, n-l-1):
            # Traverse the array from 0 to n-l-1
            # Swap if the element found is greater than the next element
            if arr[r] > arr[r+1]:
                arr[r], arr[r+1] = arr[r+1], arr[r]
                swapped = True  # Set swapped flag to True if a swap is performed
        print(arr)
        # If no swap is performed in the inner loop, the array is already sorted
        # So, we can break the outer loop
        if not swapped:
            break
x = [2,13, 4, 1, 3, 6, 28]
print('Before sorting',x)
print('After sorting',bubble_sort(x))

# Insertion Sort Algorithm TC O(N^2)
# Take an element and place it in correct position
def insertion_sort(arr):
    n = len(arr)
    for l in range(n):
        r = l
        while r>0 and arr[r-1]>arr[r]:
            arr[r-1], arr[r] = arr[r], arr[r-1] 
            r-=1
        print(arr)
    return arr
    
x = [2,13, 4, 1, 3, 6, 28]
print('Before sorting',x)
print('After sorting',insertion_sort(x))



