# input
"""
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number & 1 == 1:
    print("odd")
else:
    print("even")
"""
# while
'''
prompt = "tell me your input."
message = ""
active = True
while active:
    message = input(prompt)
    if message != "quit":
        print(message)
    else:
        break
        #active = False
'''
# 字典 列表的结构化编程
"""
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")

    if repeat == 'no':
        polling_active = False
print("\n---- Poll Results ----")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
"""

# 函数 非常灵活的使用方式 这个函数和JavaScript的函数超级类似
"""
def greet_user(username):
    print("hello, " + username.title() + "!")


greet_user("pengpeng")


def describe_pet(pet_name, animal_type='dog'):
    print(pet_name + ":" + animal_type)


describe_pet("pengpeng", "pig")


def build_person(first_name, last_name, age=31):
    person = {'first': first_name, 'last':last_name}
    return person


musician = build_person('peng', 'zhang')
print(musician)
"""


# 函数的参数 作为模块py_func在making_pizza中使用
def make_pizza(size, *toppings):
    print("size: " + str(size))
    for topping in toppings:
        print("- " + topping)
