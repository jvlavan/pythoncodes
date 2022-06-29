def gcd(a,b):
    if (a==0):
        return b
    else:
        return gcd(b%a,a)
a=int(input("Enter the number1:"))
b=int(input("Enter the number2:"))
print("The GCD of ",a," and ",b," is ",gcd(a,b))            