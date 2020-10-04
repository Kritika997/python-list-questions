negative_no = []
postive_no = []
even_no = []
odd_no = []
i = 1
while i<10:
    user_input = int(input("enter a number"))
    if user_input>0:
        postive_no.append(user_input)
    else:
       negative_no.append(user_input)
    if user_input%2==0:
        even_no.append(user_input)
    else:
        odd_no.append(user_input)
    i = i+1
print(negative_no)
print(postive_no)
print(even_no)
print(odd_no)