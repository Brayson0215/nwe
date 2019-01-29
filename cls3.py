name=input("enter the name of student")
marks=int(input("marks of the student"))
if marks>=90 and marks<=100:
    print("a")
elif marks>=70 and marks<90:
    print("b")
elif marks>=40 and marks<70:
    print("C")
else:
    print("fail")