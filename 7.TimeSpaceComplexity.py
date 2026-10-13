#7. O(1)- constant time complexity , O(1)-space complexity
'''n=int(input("Enter a number:"))
print(n+100)'''

#O(n)- linear time complexity , O(1)-space complexity
'''n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(i,end="")'''

#O(n)- linear time complexity , O(n)- linear space complexity
'''n=int(input("Enter a number:"))
arr=[]
for i in range(n):
    num=int(input("Enter a value:"))
    arr.append(num)
print("List",arr)'''

#O(n^2)- quadratic time complexity , O(1)-space complexity
'''n=int(input("Enter n:"))
num=1
for i in range(n):
    for j in range(j):
        print(num,end=" ")
        num+=1
    print()'''

#O(log(n))-logarithmic time complexity,O(1)-space complexity
'''n=int(input("Enter a value:"))
while n>1:
    print(n)
    n//=2
print(1)'''

#O(n(logn))- constant time complexity , O(1)-space complexity
'''n=int(input("Enter a value:"))
for i in range(n):
    j=n
    while j>1:
        j//=2
print("Done")'''

#O(2^n)-exponential time complexity
def count(n):
    if n==0:
        return 1
    return count(n-1)+count(n-1)
n=int(input("Enter a number:"))
print("result:",count(n))
