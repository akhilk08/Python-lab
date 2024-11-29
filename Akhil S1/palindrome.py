def is_palindrome(n):
    n_str=str(n)
    n_rev=n[slice(None, None, -1)]
    if n_str==n_rev:
        print("The number ",n_rev," is PALIDROME!")
    else:
        print("The number ",n_str," is NOT PALINDROME")
n=input("Enter any number: ")
is_palindrome(n)
