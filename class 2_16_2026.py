#1. Reverse a String
#Write a Python function to reverse a given string.
#Input: "hello"
#Output: "olleh"

input = "hello"
rev_input = ""

word = len(input) - 1

while word > 0:
    rev_input = rev_input + input[word]
    word = word - 1
print(rev_input)

#2. Check for Anagrams
#Write a Python function to check if two given strings are anagrams of each other.
#Input: "listen", "silent"
#Output: True

input_1 = "listen"
input_2 = "silent"

if len(input_1) != len(input_2):
    print(False)
else:
    counts= {}
    for letter in input_1:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
anagram = True

#sub letters using second string

for letter in input_2:
    if letter not in counts:
        anagram = False
        break
    else:
        counts[letter] -= 1

for value in counts.values():
    if value !=0:
        anagram = False
        break

print(anagram)

#3. Remove Duplicate Characters
#Write a Python function to remove all duplicate characters in a given string while preserving the order of the remaining characters.
#Input: "programming"
#Output: "progamin"

input = "programming"
result = ""

for letter in input:
    if letter not in result:
        result = result + letter
print(result)