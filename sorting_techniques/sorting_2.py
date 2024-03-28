# Merge Sort Algorithm => Divide and merge recursively
# TC O(nlogn) SC O(n)

def merge_sort(arr):
    # Check if the array has more than one element
    if len(arr) > 1:
        # Find the middle index of the array
        mid = len(arr) // 2
        # Divide the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively sort the left half
        merge_sort(left_half)
        # Recursively sort the right half
        merge_sort(right_half)
        
        # Merge the sorted halves
        # Initialize pointers for the left, right, and merged arrays
        i = j = k = 0
        
        # Compare elements from left_half and right_half and merge them into arr
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Copy the remaining elements of left_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Copy the remaining elements of right_half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1 
    
arr = [9, 4, 7, 6, 3, 1, 5]
n = len(arr)
print('Before sorting',arr)
merge_sort(arr)
print('After sorting',arr)


