#doing without function
# a = 34
# b = 76
# c = 34

# average = (a + b + c)/ 3
# print(average)

#doing with function

#function definition
def avg():
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    c = int(input("Enter your third number: "))

    average = (a+b+c)/3
    print(average)

#function calling
avg()
print("Calculating average again")
avg()
print("Calculating average again")
avg()
print("end of the program")