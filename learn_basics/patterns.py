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
