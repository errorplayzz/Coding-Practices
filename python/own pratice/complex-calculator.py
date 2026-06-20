from unittest import case


a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
c=input("Enter a operator(+, -, *, /): ")

if c == "+":
    print("Addition: ", a + b)
elif c == "-":
    print("Subtraction: ", a - b)
elif c == "*":
    print("Multiplication: ", a * b)    
elif c == "/":
    print("Division: ", a / b)    
else:    print("Invalid operator") 