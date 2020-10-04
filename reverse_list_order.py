i = 1
num_reverse= []
num = []
while i<=5:
    user_input = int(input("enter a number"))
    num.append(user_input)
    i = i+1
print(num)
i = 1
while i<=len(num):
    num_reverse.append(num[-i])
    i = i+1
print(num_reverse)
    
