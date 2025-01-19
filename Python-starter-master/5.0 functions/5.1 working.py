def odd_sum():
    sum=0
    i=1
    while i<=15:
        if i%2!=0:
            sum+=i
        i+=1
    print(sum)
#odd_sum()

def is_prime():
    number=int(input("enter a number to check if it is a prime number: "))
    for i in range(2,number-1):
        if number%i==0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")
#is_prime()


#                               FUNCTIONS WITH PARAMETERS
# function for name age school department and generate story
def band_name(name,age,school,department):
    print(f"My name is {name}, i am {age} years old and i school in {school} in the department of {department}")
#band_name(name="faith",age=18,school="NAHPI",department="COMPUTER ENGINEERING")
name=input("enter your name: ")
age=input("enter your age: ")
school=input("enter your school: ")
department=input("enter your department: ")
band_name(name,age,school,department)
