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
           print(start, end='')
           start = 1-start
        print() 

binary_triangle(5)

