student= dict()
n = int(input("Enter number of students :"))

for i in range(0,n):
	x, y = input("Enter name of student(First and last name): ").split()
	z = input("Enter age: ")
	m = input("Enter grade: ")
	student[x, y] = (z, m)
	
def sort():
	ls = list()
	
	for sname,details in student.items(): 
	
		tup = (sname[0],sname[1]) 	
		ls.append(tup) 
		
	ls = sorted(ls) 
	for i in ls:
	
		print(i[0],i[1]) 
	return

def mingrade():
	ls = list()

	for sname,details in D.items(): 
		ls.append(details[1]) 
	
	ls = sorted(ls) 
	print("Minimum grade: ", min(ls))
	return

def searchdetail(fname):
	ls = list()
	
	for sname,details in student.items():
	
		tup=(sname,details)
		ls.append(tup)
		
	for i in ls: 
		if i[0][0] == fname:
			print(i[1][0])
	return
