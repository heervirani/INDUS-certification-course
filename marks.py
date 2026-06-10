s1=int(input("Enter marks1:"))
s2=int(input("Enter marks2:"))
s3=int(input("Enter marks3:"))
s4=int(input("Enter marks4:"))
s5=int(input("Enter marks5:"))
avg=(s1+s2+s3+s4+s5)/5
perc=((s1+s2+s3+s4+s5)/500)*100
print("Average of marks:",avg)
print("Percentage of marks:",perc)

if perc>=80 and perc<=100:
    print("A Grade")
elif perc>=60:
    print("B Grade")
elif perc>=40:
    print("C Grade")
else:
    print("Student FAil")
