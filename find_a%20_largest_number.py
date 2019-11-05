user_input=input("please enter some number ")
max = user_input[0]
for number in user_input:
    if number > max:
        max = number
print(max)