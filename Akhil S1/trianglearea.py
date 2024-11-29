a=int(input("Enter first side of triangle :"))
b=int(input("Enter second side of triangle :"))
c=int(input("Enter third side of triangle :"))

s=(a+b+c)/2

print("Semiperimeter of triangle =",s)

x=(s*(s-a)*(s-b)*(s-c))**0.5
 
print("Area of triangle =",x)
 
