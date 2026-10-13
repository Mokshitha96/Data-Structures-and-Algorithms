#9.Naive approach-find occurences of a number
arr=list(map(int,input("Enter elements:").split()))
value=int(input("Enter value:"))
count=0
for i in arr:
    if i==value:
        count+=1
print(value,"Occurences are:",count)
    
