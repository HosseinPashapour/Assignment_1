print("Educational status")
name = input("Enter your name :")
family = input("Enter your family :")


a = float(input("Enter First  Score: "))
b = float(input("Enter Second  Score: "))
c = float(input("Enter Third  Score: "))

#calculate average
avg = (a+b+c) / 3
if avg>=17:
    result = "Great"
elif avg<17 and avg>=12:
    result = "Normal"
elif avg<12:
    result = "Fail"

print("Student :",name,family,"| Educational status:",result)