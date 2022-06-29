from re import T


a=int(input("Enter the value  for a:"))
b=int(input("Enter the value  for b:"))
def swap(x,y):
    global a
    global b
    t=a
    a=b
    b=t
    
print("The value of a and b before swaping:",a,b)
swap(a,b)
print("The value of a and b after swaping:",a,b)