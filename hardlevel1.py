a2 = int(input("Enter a2: "))
a1 = int(input("Enter a1: "))
b = int(input("Enter b: "))
c1 = (a1+b)%10
c2 = a2+(a1+b)/10
print("result number of tens %.f" %c2)
print("result number of units %.f" %c1)