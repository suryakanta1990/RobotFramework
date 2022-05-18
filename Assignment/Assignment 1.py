# Check the given number is positive or negative?
# Check the largest of two numbers?
# Check the largest of three numbers?
# Print week no if you provide week name as input?

# NO-1
a=20
print("Given number is positive")if a>=0 else print("given number is negetive")

num1=int(input("enter a number"))
if num1>=0:
    print("positive")
else:
    print("negetive")

# NO-2

a=20
b=10
if a>b:
    print("given no is large:",a)
elif b>a:
    print("given no is lage:",b)
else:
    print("error")

# NO-3

Num1=int(input("Enter first number"))
Num2=int(input("Enter second number"))
Num3=int(input("Enter third number"))
if (Num1>Num2) and (Num1>Num3):
    print("Large is:",Num1)
elif (Num2>Num1) and (Num2>Num3):
    print("Large is:",Num2)
elif Num1==Num2==Num3:
    print("All are equal")
else:
    print("Large no is:",Num3)
#No-4


weekname=input("Enter week name:"+" ")

if weekname=="sunday":
    print(1)
elif weekname=="monday":
    print(2)
elif weekname=="tuesday":
    print(3)
if weekname=="wednesday":
    print(4)
elif weekname=="thursday":
    print(5)
elif weekname=="friday":
    print(6)
elif weekname=="saturday":
    print(7)
else:
    print("wrong input")