#Question 1 > String cleaning and transformation

## Remove all vowels

s= "data engineering rocks" #a,e,i,o,u
count = 0
for ch in s:
    if ch == 'e' or ch == 'a' or ch == 'i' or ch == 'o' or ch == 'u':
        count = count + 1
print(count)

#Replace spaces with underscores

word =  "data engineering rocks"
new_word = ""
for letter in word:
    if letter == " ":
        new_word = new_word + "_"
    else:
        new_word = new_word + letter
print(new_word)

#For title use

sentence = "data engineering rocks"
new_sentence = sentence.title()
print(new_sentence)

#Given a list of dictionaries representing sales transactions:
sales = [
  {"product": "Pen", "amount": 10},
  {"product": "Book", "amount": 20},
  {"product": "Pen", "amount": 15},
  {"product": "Pencil", "amount": 5}
]

totals = {}  # empty dictionary to store totals

for item in sales:
    product_name = item["product"]
    amount = item["amount"]

    if product_name in totals:
        totals[product_name] = totals[product_name] + amount
    else:
        totals[product_name] = amount

# Print results
for product in totals:
    print(product + ":", totals[product])



#Write a Python function that takes a list of integers and returns a new list containing
#lements that appear exactly once.
#xample:
#nput: [4, 5, 4, 6, 7, 5, 8]
#utput: [6, 7, 8]

numbers = [4, 5, 4, 6, 7, 5, 8]

result = []

for num in numbers:
    if numbers.count(num) == 1:
        result.append(num)

print(result)