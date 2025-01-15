#name=input("enter your name ").lower()
#if name=="jude":
#    print("teacher")
#else:
#    print("your are from mile six")  
#the modulus, "%", finds the remainder when two numbers are divided
#num=int(input("enter a number to check if it is even or odd: "))
#if num%2==0:
#    print("even")
#else:
#    print("odd")


height=float(input("enter your height "))
if height>=1.5:  
    age=int(input("enter your age "))
    if age<14:
        print("under 14")
    elif age<16:
        print("under 16")
    elif age<19:
        print("under 18")
        gender=input("enter your gender ")                                                                                                                                                     
        if gender=="female":                                                                                                
            print("you are eligible")
        else:
            print("you are not a female. Go home") 
    else:
        print("you are too old. Go home")
else:
    print("you are too short. Go home")                           