def reverse(s):
    return s[::-1]
s=str(input("enter the string input to which the palindrome has to be found"))
rev=reverse(s)
if s==rev:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
