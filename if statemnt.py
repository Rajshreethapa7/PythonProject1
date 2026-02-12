operator = input("what arthemtic operation'+,-,*,/?:  ")
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

if operator == "+":
  result = num1 + num2
  print(result)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
   print(f"{operator} is an invalid operator")

## python weight convertor


