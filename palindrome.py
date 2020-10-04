name=[ 'n', 'i', 't', 'i', 'n' ]
name1 = []
i = 0
while i<len(name):
    if name[i]==name[i]:
        name1 = name[i]
        print(name[i])
        i = i+1
i = 0
while i<len(name):
    if name[-i]==name1[i]:
        reverse = name[-i]
        i = i+1
if name1==reverse:
    print("yes it is palindrome")
else:
    print("no it is not palindrome")
        




        