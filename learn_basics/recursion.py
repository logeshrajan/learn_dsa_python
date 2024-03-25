# Understand Recursion by printing something N times
def printNos(x: int) -> List[int]: 
    # Write your code here
    # return list(range(1, x+1))
    if x == 0:
        return []
    else:
        prev_list = printNos(x-1)
        prev_list.append(x)
        return prev_list

# Print Name N times using Recursion
def printNos(n, name):
    prev_list = []
    if n == 0:
        return []  # Base case: return an empty list when x is 0
    else:
        previous_list = printNos(n - 1, name)  # Recursively call the function with x-1
        print(name)
        return 

n = 5
result = printNos(n, 'Logesh')

# Print 1 to N using Recursion
def printNtimes(n):
    if n==0:
        return
    else:
        printNtimes(n-1)
        print(n)
printNtimes(10)

def printNtimes_back_tracking(i,n):
    if i > n:
        return
    print(i)
    printNtimes_back_tracking(i+1, n)
    
printNtimes_back_tracking(1, 10)

# Print N to 1 using Recursion
def printNtimes(n):
    if n==0:
        return
    else:
        print(n)
        printNtimes(n-1)
# printNtimes(10)

def printNtimes_back_tracking(i,n):
    if i > n:
        return
    printNtimes_back_tracking(i+1, n)
    print(i)
printNtimes_back_tracking(1, 10)

# Sum of first N Natural Numbers
def sum_n_natural_numbers(n):
    if n == 1:
        return 1
    return  n + sum_n_natural_numbers(n-1)
    
print(sum_n_natural_numbers(5))

def sum_n_natural_numbers_1(n):
    return n*(n+1)//2 # maths formula
    
print(sum_n_natural_numbers_1(5))

def sum_n_natural_numbers_2(n,total):
    if n < 1:
        return total
    else:
        return sum_n_natural_numbers_2(n-1,total+n)
    
print(sum_n_natural_numbers_2(5,0))

# Sum of first N Natural Numbers
def factorial_1(n):
    total = 1
    for i in range(2,n+1):
        total *=i
    return total
    
print(factorial_1(5))

def factorial_2(n):
    if n ==1:
        return 1
    return n * factorial_2(n-1)
print(factorial_1(3))


def factorialNumbers(n):
    def factorial(n):
        if n ==1:
            return 1
        return n * factorial(n-1)

    res = []
    i = 1
    while True:
        fact = factorial(i)
        if fact <=n:
            res.append(fact)
            i+=1
        else:
            break
    return res



