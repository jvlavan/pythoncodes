from numpy import float64


a=int(input("Enter the value  for n:"))
x=float(input("Enter the value  for x :"))
n=sum=0
def fact(num):
    if (num==1) or (num==0):
        return 1
    else:
        return(num*fact(num-1))    

for i in range(1,a+1,2):
    sum+=((-1)**n)*((x**i)/(fact(i)))
    n+=1
if ((sum<=1) and (sum>=-1)):    
    print("sin({}) is {}".format(x,sum))