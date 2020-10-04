num = [4,87,98,46,2,34,64,756,23,15,87,0]
# program for sum.
sum = 0
i = 0
while i<len(num):
    sum = sum+num[i]
    i = i+1
print(sum)

# program for average 

average = 0
average = sum//len(num)
print(average)

#  program for largr_no
large_no = 0
i = 1
while i<len(num):
    if num[i]>large_no:
        large_no = num[i]
    i = i+1
print(large_no)

# program for smallest_no
small_no = num[0]
i = 0
while i<len(num):
    if num[i]<small_no:
        small_no = num[i]
    i = i+1
print(small_no)