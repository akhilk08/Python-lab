print("Swapping variables using temporary variable")

a=10
b=5
print("a before swapping",a)
print("b before swapping",b)

temp=a
a=b
b=temp

print("a after swapping",a)
print("b after swapping",b)

print("Swapping variables without using temporary variable")

print("a before swapping",a)
print("b before swapping",b)

a=a+b
b=a-b
a=a-b

print("a before swapping",a)
print("b before swapping",b)
