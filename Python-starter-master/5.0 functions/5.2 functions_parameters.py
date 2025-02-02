# def say_name(name1,name2):
#     name_one=name1.title()
#     name_two=name2.title()
#     return f"{name_one} {name_two}"
# first_name=input("enter your first name: ")
# second_name=input("enter your second name: ")
# result=say_name(first_name, second_name)
# print(result)

def loop_number():
    sum=0
    for i in range(7):
        if i==5:
            return
        print(F"the value is {i}")
        sum+=i
    return sum
results=loop_number()
print(results)