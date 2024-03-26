# Count frequency of each element in the array
Bruteforce approach
# Hashing TC O(Q*N) SC O(N)
def find_number_of_times(nums, queries):
    res = []
    for n in queries:
        count = 0
        for num in nums:
            if n == num:
                count+=1
        print(f"{n} appears {count} times.")
        
nums = [10,5,10,15,10,5]
queries = [10,5,15,100,0,32]

find_number_of_times(nums, queries)

# Hashing TC O(N) SC O(N)
def find_number_of_times(nums, queries):
    res = {}
    for num in queries:
        res[num] = res.get(num,0)+1
    for k,v in res.items():
        print(f"{k} appears {v} times.")
        
nums = [10,5,10,15,10,5]
queries = [10,5,15,100,0,32]

find_number_of_times(nums, queries)
