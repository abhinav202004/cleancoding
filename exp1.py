a=int(input("enter first number: "))
b=int(input("enter second number: "))
choice=int(input("enter choice: "))
if choice==1:
    c=a+b
    print("{0}+{1}={2}".format(a,b,c))
elif choice==2:
    c=a-b
    print("{0}-{1}={2}".format(a,b,c))
elif choice==3:
    c=a*b
    print("{0}x{1}={2}".format(a,b,c))
elif choice==4:
    c=a/b
    print("{0}/{1}={2}".format(a,b,c))
else:
    print("invalid choice")