#program to print table
a=int(input("Enter the number to print table:"))
b=int(input("Enter the limit of the table:"))
for i in range(1,b+1):
    print(a,"x",i,"=",a*i)
    