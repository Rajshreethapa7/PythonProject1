
numbers = [10,20,20,30]
d={}
for num in numbers:
    if num in d:
        d[num] = d[num] + 1
else: d[num] = 1
print(d)

freq = 0
max=0
for key in d.keys():
   value = d[key]
   if value > freq:
       max = key
       freq = value
print(max)

line = "hello world hi world hi nepal"
words =line.split(' ')
print(words)

word_counts={}
for word in words:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1
print(word_counts)

#set- cant store duplicate value

list = [1,2,2,3,4,4,5]
s = set(list)
print(s)

list = [5,3,1,2,2,3,4,4,5]
result = sorted(set(list))
print(result)