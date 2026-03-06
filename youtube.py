unit = input("is this temperature in celsisus or fahrenhiet")
temp = input(input("enter the temperture"))

if unit == "celsius":
    pass
elif unit == "fahrenheit":
    pass
else:
    print(f"{unit} is not a valid unit")
    #temperature conversion program

#logical operators = or , and , not

temp = 35
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("the outdoor event is cancelled")
else:
    print("the outdoor even is still scheduled")

#and operator

temp = 30
is_sunny = True

if temp >= 28 and is_sunny:
    print("it is hot outside")
    print("it is sunny)")
elif temp <= 0 and is_sunny:
    print("it is cold outside")
    print("it is sunny)")


# strings different methods
#LENGHT of a string len()
#find the integer value of a string(variablename.find)
#find the reverse variablename.rfind
#name = name.capitalize
#name = name.upper()- all characters will be upper
#name = name.lower()- all characters will be lower
#result = name.isdigit()- will return true or false if the value entered is all digits
#esult= name.isalpha()- will return value true or flase if return alphabets
#result = phone_num.count("_")- it counts how many characters within a string.
#phone_number.replace("-", " ") - to replace a character within a string
#print(help(str))- will give all the strings available in pycharm

##exercise

username = input("enter a username")

if len(username) >12:
    print ("your username is too long")
elif not username.find(" ") == -1:
    print("your username cant contain spaces")
elif not username.isalpha():
    print("your username cant contain numbers")
else:
    print(f"welcome {username}")

## string indexing = [start: end : step)

credit_num = "1234-3456-0493-2383"

print(credit_num[4])
#[0:4] - 1234
#[:4] - 1234
#[5:9]-3456
#[5:]- prints everything excepts first 4
#[-1] - 3
#[::] - everything is printed
#[::3] - skips 3
#[-4:] - prints last 4 digits

#email slicer

email = input ("enter your email: ")
index = email.index("@")

username = email[:index]
domain = email[index+1:]

print(f"your username is {username} and domain is {domain}")

# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :0(number) = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
# :% = percentage format

price1 = 3.14159
price2 = -987.65
price3 = 12.34
print(f"price1 is: ${price1:}")
print(f"price2 is: ${price2:}")
print(f"price3 is: ${price3:}")

#while loop = perform some code WHILE some condition remains true
name = input("Enter your name: ")

while name == "": #while this conditionas is true run until its false
    print("you didn't enter your name")
    name = input("Enter your name: ")
print(f"hello {name}")
#------------
age = int(input("enter your age: "))

while age < 0: #age is less than zero
    print ("age cant be negative")
    age = int(input("enter your age: "))

print(f"your age is {age}")

#for loops = execute a block of code a fixed number of times.
#You can iterate over a range, string, sequence, etc.

for x in range(1,21):
    if x ==13:
        continue #continue keyword used to skip a iteration break keyword can be used to stop
    else:
        print(x)
# nested loop = A loop within another loop (outer, inner)
#                          outer loop:
#                              inner loop:
for x in range(1,10):
        print(x, end=" ") #prints number in horizontal in place of vertical

#


