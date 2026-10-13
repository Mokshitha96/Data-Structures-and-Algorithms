#8.Math approach-Strong number
'''n=int(input("Enter a number:"))
copy=n
total=0
while n!=0:
    d=n%10
    f=1
    i=1
    while i<=d:
        f*=i
        i+=1
    total+=f
    n//=10
if total==copy:
    print(copy,"is a strong number")
else:
    print(copy,"is not a strong number")'''


#1/2!+2/3!+3/4!+4/5!+........
n=int(input("enter a number:"))
total=0
f=1
for i in range(1,n+1):
    f*=i+1
    total+=i/f
print("sum:",total)
