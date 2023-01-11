
try:
    a= float(input("enter the number"))
    b=float(input("enter the second number"))
except Exception as e:
    print(e)
else:
    sum=a+b
    print(sum)


