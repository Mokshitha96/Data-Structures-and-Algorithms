#2.Write a program to reverse a number
'''n=int(input("Enter a number:"))
while n!=0:
    d=n%10
    print(d,end='')
    n//=10'''

#2nd method
n=int(input("Enter a number:"))
rev=0
while n!=0:
    d=n%10
    rev=(rev*10)+d
    n//=10
print(rev)
