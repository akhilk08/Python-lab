n=int(input("Enter limi: "))
student={}
for i in range (0,n):
	name=input("name: ")
	age=input("age: ")
	gr=input("grade: ")
	student[name]={age,gr}
print(student)
