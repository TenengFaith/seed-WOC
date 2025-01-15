height=float(input("enter your height in meters: "))
weight=float(input("enter your weight: "))
bmi=weight/height**2
print(f"your bmi is {bmi}")
if bmi<18.5:
    print("your are underweight")
elif bmi<25:
    print("normal weight")
elif bmi<30:
    print("you are slightly overweight")
elif bmi<35:
    print("you are obessed")
else:
    print("you are clinically obessed")