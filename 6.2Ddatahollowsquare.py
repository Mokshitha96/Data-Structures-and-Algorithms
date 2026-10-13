#6.2D data hollow square pattern with *
'''n=int(input("Enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#2D data with diagonal intersection in  hollow square pattern using * 
'''n=int(input("Enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


#2D data hourglass in  hollow square pattern using * 
'''n=int(input("Enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#2D data hollow square pattern using * with intersection at the middle
'''n=int(input("Enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==n//2 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#2D data hollow square pattern using * with * in the pattern
'''n=int(input("Enter n:"))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1 or i==n//2 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
