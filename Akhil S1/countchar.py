def str_count(string):
	count=0
	for char in string[0:]:
		if char!='':
			count +=1
	return count
string=input("Enter the string:")
print(f"The string contains {str_count(string)} letters")
