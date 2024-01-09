print("Sanjesh BMI")
a=float(input("Vazn (K.g):"))
b=float(input("Gad(C.m):"))
BMI=a/b**2
print("BMI=",BMI)
if BMI<18.5:
    result=("underweight")
elif 25>BMI>=18.5:
    result=("normal weight")
elif 30>BMI>=25:
    result=("overweight")
elif 35>BMI>=30:
    result=("obesity")
elif 40>BMI>35:
    result=("extreme obesity")
print(result)