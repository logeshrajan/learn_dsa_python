# Count digits in a number
# T O(nlog10n)  S O(1)
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

# T O(nlog10n)  S O(1)
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
# T O(nlog10n)  S O(1)
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

