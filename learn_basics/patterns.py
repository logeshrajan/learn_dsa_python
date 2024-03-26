# Pattern – 1: Rectangular Pattern

n = 100

for row in range(n+1):
    # print('row',row)
    for col in range(n+1):
        # print('col',col)
        print('*',end='')
    print()

# Pattern-2: Right-Angled Triangle Pattern

n = 4
for row in range(1,n+1):
    # print('row',row)
    for col in range(1,row+1):
        # print('col',col)
        print('*',end=' ')
    print()
# Pattern – 3: Right-Angled Number Pyramid    
for row in range(1,n+1):
    # print('row',row)
    for col in range(1,row+1):
        # print('col',col)
        print(col,end=' ')
    print()    

# Pattern – 4: Right-Angled Number Pyramid – II
n = 4
for row in range(1,n+1):
    # print('row',row)
    for col in range(1,row+1):
        # print('col',col)
        print(row,end=' ')
    print()    

# Pattern-5: Inverted Right Pyramid
n = 4
for row in range(n,0,-1):
    # print('row',row)
    for col in range(row,0,-1):
        # print('col',col)
        print('*',end=' ')
    print()    

# Pattern – 6: Inverted Numbered Right Pyramid
n = 5
for row in range(n,0,-1):
    # print('row',row)
    for col in range(1,row+1):
        # print('col',col)
        print(col,end=' ')
    print()    

# Pattern – 7: Star Pyramid
n = 5
for row in range(1,n+1):
    # print('row',row)
    for space in range(0,n-row):
        print(' ', end='')
    for col in range(1,2*row):
        # print('col',col)
        print('*',end='')
    for space in range(0,n-row):
        print(' ', end='')
    print() 

# Pattern – 8: Inverted Star Pyramid
n = 5
for row in range(n,0,-1):
    # print('row',row)
    for space in range(0,n-row):
        print(' ', end='')
    for col in range(1,2*row):
        # print('col',col)
        print('*',end='')
    for space in range(0,n-row):
        print(' ', end='')
    print() 

# Pattern – 9: Diamond Star Pattern
def inverted_pyramid(n):
    for row in range(n,0,-1):
        # print('row',row)
        for space in range(0,n-row):
            print(' ', end='')
        for col in range(1,2*row):
            # print('col',col)
            print('*',end='')
        for space in range(0,n-row):
            print(' ', end='')
        print() 
        
def normal_pyramid(n):
    for row in range(1,n+1):
    # print('row',row)
        for space in range(0,n-row):
            print(' ', end='')
        for col in range(1,2*row):
            # print('col',col)
            print('*',end='')
        for space in range(0,n-row):
            print(' ', end='')
        print() 

normal_pyramid(5)        
inverted_pyramid(5)

# Pattern – 10: Half Diamond Star Pattern

def half_dimond(n):
    for row in range(1,2*n):
        if row<=n:
            stars = row
        else:
            stars = 2*n-row
        # print(stars)
        for star in range(1,stars+1):
            print('*', end='')
        # print(star)
        for space in range(1,n-stars):
            print('', end='')
        print() 

half_dimond(10)

# Pattern – 11: Binary Number Triangle Pattern

def binary_triangle(n):
    for row in range(1,n+1):
        if row%2 ==0:
            start = 0
        else:
            start = 1
        for col in range(row):
           print(start, end=' ')
           start = 1-start
        print() 

binary_triangle(5)

# Pattern – 12: Number Crown Pattern
def pattern12(n ):
    spaces = 2*(n-1)
    for row in range(1,n+1):
        for num in range(1,row+1): # to print number in each row before space
            print(num, end=' ')
        for space in range(spaces): # to print spaces
            print(' ', end='')
        for num in range(row,0,-1): # to print number in each row after space
            print(num, end=' ')
        print()
        spaces-=2
pattern12(4)

# Pattern – 13: Increasing Number Triangle Pattern
def pattern13(n ):
    num = 1
    for row in range(1, n+1):
        for col in range(1,row+1):
            print(num, end=' ')
            num+=1
        print()
        
pattern13(4)

# Pattern-14: Increasing Letter Triangle Pattern
def pattern14(n):
    for row in range(1, n + 1):  # Outer loop for rows
        for ind in range(1, row + 1):  # Inner loop for each row
            print(chr(64 + ind), end=" ")  # Print the character corresponding to the ASCII value
        print()  # Move to the next line after each row

# Pattern-15: Reverse Letter Triangle Pattern
def pattern15(n):
    for row in range(n, 0,-1):
        for ind in range(1, row + 1):  # Inner loop for each row
            print(chr(64 + ind), end=" ")  # Print the character corresponding to the ASCII value
        print()
        
# Pattern – 16: Alpha-Ramp Pattern
def pattern16(n):
    for row in range(1,n+1):
        for ind in range(1, row + 1):
            print(chr(64 + row), end=" ")
        print()
        
pattern16(4)

# Pattern – 17: Alpha-Hill Pattern
def pattern17(n):
    for i in range(n):
        print(" " * (n - i - 1), end="")
        for j in range(i + 1):
            print(chr(65 + j), end=" ")
        print(" " * (n - i - 1), end="")
        for j in range(i - 1, -1, -1):
            print(chr(65 + j), end=" ")
        print()
        
# Pattern-18: Alpha-Triangle Pattern
def pattern18(n):
    for row in range(1,n+1):
        for col in range(row):
            print(chr(64+n-col), end=' ')
        print()

pattern18(3)

# Pattern-19: Symmetric-Void Pattern
def pattern19(n):
    space = 0
    for row in range(n):
        for st in range(n-row):
            print('*', end='')
        for sp in range(0,space):
            print(' ', end='')
        for st in range(n-row):
            print('*', end='')
        space+=2
        print()
    space = (2*n)-2
    for row in range(n):
        for st in range(row+1):
            print('*', end='')
        for sp in range(0,space):
            print(' ', end='')
        for st in range(row+1):
            print('*', end='')
        space-=2
        print()
pattern19(5)

# Pattern – 20: Symmetric-Butterfly Pattern

def pattern20():
    space = (2*n)-2
    for row in range(n):
        for st in range(row+1):
            print('*', end=' ')
        for sp in range(0,space):
            print(' ', end=' ')
        for st in range(row+1):
            print('*', end=' ')
        space-=2
        print()
    space = 2
    for row in range(1,n):
        for st in range(n-row):
            print('*', end=' ')
        for sp in range(0,space):
            print(' ', end=' ')
        for st in range(n-row):
            print('*', end=' ')
        space+=2
        print()

# Pattern – 21: Hollow Rectangle Pattern
def pattern21(n):
    for row in range(n):
        for col in range(n):
            if row ==0 or col ==0 or row == n-1 or col == n-1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
                
pattern21(4)

# Pattern – 22: The Number Pattern
def pattern22(n):
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            top = i
            bottom = j
            right = (2 * n - 2) - j
            left = (2 * n - 2) - i
            print(n - min(min(top, bottom), min(left, right)), end=" ")
        print()
                
pattern22(3)












