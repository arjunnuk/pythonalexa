li=[]
n=int(input("enter the value of n"))
for i in range(0,n):
    print("enter the element here",i+1)
    x=int(input())
    li.append(x)
print(li)
psum=0
nsum=0
for i in li:
    if(i>0):
        psum=psum+i
    else:
        nsum=nsum+i
print("the sum of positive number is",psum)
print("the sum of negative number is",nsum)
name="Arjun uk"
usn="19mca07"
