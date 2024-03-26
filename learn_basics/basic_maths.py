# Count digits in a number
# T O(log n)  S O(1)
def count_digits(n): 
   count=0
   x=n
   while( x != 0 ):
       x//=10
       count+=1
   return count
n = 54343
print("Number of digits in ",n," is ",count_digits(n)) 

# T O(1)  S O(1)
def count_digits(n):
      return len(str(n))
print("Number of digits in ",n," is ",count_digits(n)) 

# T O(log n)  S O(1)
# Problem Statement: Given a number N reverse the number and print it.
def reverse_number(n):
    reverse = 0
    while n>0:
        last_digit = n%10
        reverse = reverse * 10 + last_digit
        n //=10
    return reverse
    # return int(str(n)[::-1])
print(reverse_number(123))

# Polindrome
# T O(log n)  S O(1)
def reverse_number(n):
    reverse = 0
    old_n = n
    while n>0:
        last_digit = n%10
        reverse = reverse * 10 + last_digit
        n //=10
    return reverse
    # return int(str(n)[::-1])
n = 121
if reverse_number(n)==n:
    print(f"{n} is Palindrome")
else:
    print(f"{n} is not Palindrome")

# Amstrong

def is_amstrong(n):
    """
    Armstrong Numbers are the numbers having the sum of digits raised to power no. of digits is equal to
    a given number. Examples- 0, 1, 153, 370, 371, 407, and 1634 are some of the Armstrong Numbers.
    """
    old_n = n
    l_n = len(str(n))
    res = 0
    while n>0:
        res += (n%10)**l_n
        n//=10
    if old_n == res:
        return f"yes {old_n} is an Amstrong number" 
    else:
        return f"yes {old_n} is Not an Amstrong number"
    
print(is_amstrong(153))

# Print All Divisor
def printDivisorsOptimal(n):
    print("The Divisors of",n,"are:")
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            print(i, end=" ")
            if i != n/i:
                print(int(n/i), end=" ")
    print()
printDivisorsOptimal(36)

# Is Prime or not

n = int(input())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

if is_prime(n):
    print('YES')
else:
    print('NO')
