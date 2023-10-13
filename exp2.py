std_ne=input(" enter your name: ")
stdt_Rno=int(input("enter your roll no:  "))
std_C=input("enter your class ")
Mk_Pyt=int(input("enter python marks:  "))
Mk_Ja=int(input("enter Java marks:   "))
Mk_DS=int(input("enter Data Science marks:   "))
Mk_HTML=int(input(" enter HTML marks:  "))
Mk_CSS=int(input(" enter CSS marks:  "))
total=(Mk_Pyt+Mk_Ja+Mk_DS+Mk_HTML+Mk_CSS)
print(total)
percentage=(total/500)*100
print(percentage)
if percentage>=90:
    print("A+ Grade")
    print("Very Good")
elif percentage >=80:
    print("A Grade")
    print("Good")
elif percentage >=70:
    print("B+ Grade")
    print("Average")
elif percentage >=60:
    print("B Grade")
    print("Below Average")
else:
    print("U Grade")
    print("RA")
