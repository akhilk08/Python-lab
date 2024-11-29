n=int(input("Enter the limit:"))
names=[]
for i in range(n):
	name=input(f"Enter name{i+1}:")
	names.append(name)
	names.sort()
print(f"sorted list:\n{names}")
