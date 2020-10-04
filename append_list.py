# user_input = int(input("enter a number"))
# i = 1
# list = []
# while i<=5:
#     user_input = int(input("enter a number"))
#     list.append(user_input)
#     i = i+1
# print(list)
user_input = int(input("enter a number"))
i = 1
list = []
while i<5:
    user_input = int(input("enter a number"))
    list.append(user_input)
    i = i+1
print(list)
user_input1 = int(input("enter a number"))
if user_input1 in list:
    print(user_input1)
else:
    print("nahi hai")