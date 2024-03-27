# Selection Sort Algorithm
# get the minimum and swap it to left index. then increment the left index by 1.
TC O(N^2) SC O(1)
def selection_sort(arr):
    for l in range(len(arr)-1):
        min_val = l
        for r in range(l,len(arr)):
            if arr[r] < arr[l]:
                min_val = r
        arr[min_val], arr[l]= arr[l], arr[min_val]
    return arr
x = [7, 5, 9, 2, 8]
print('Before sorting',x)
print('After sorting',selection_sort(x))

