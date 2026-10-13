#4.print odd numbers from set of natural numbers
n=int(input("Enter n: "))
for i in range(1,n+1):
    if i%2==1:
        print(i,end='')
