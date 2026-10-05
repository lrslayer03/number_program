n=int(input("enter a number : "))
m=n
rev=0
while n!=0:
    d=n%10
    rev=rev*10+d
    n=n//10

if rev==m:
    print(m,"is palindrome number")
else:
    print(m,"is not paindrome number")
    