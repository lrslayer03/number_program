n1=int(input("Enter big number : "))
n2=int(input("Enter small number : "))
a=n1
b=n2
while n2!=0:
    n3=n2
    n2=n1%n2
    n1=n3

HCF=n1
print("HCF =",HCF)

