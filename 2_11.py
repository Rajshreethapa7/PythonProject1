from operator import truediv


def sum_of_2_num_equals_to_target(list, target):
    for i in range (0,len(list)):
        for j in range (i+1,len(list)):
            if i!=j:
                if list[i] + list[j]==target:
                    return True
    return False
list = [1,2,3]

s= "hello world" #a,e,i,o,u
count = 0
for ch in s:
    if ch == 'e' or ch == 'a' or ch == 'i' or ch == 'o' or ch == 'u':
        count = count + 1
print(count)

s= "hello world"
count = 0
vowels = set('aeiou')
for ch in s:
    if ch in vowels:
        count = count + 1
print(count)


