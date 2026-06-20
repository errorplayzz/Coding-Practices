a = int(input("Enter your age: "))

if(a>18):
    print("You are above the age of consent")
    print("Good for you")

elif(a==18):
    print("You are entering the age of consent")
    print("Good for you")
elif(a<0):
    print("You are entering an negative age")
    print("Please enter a valid age")
elif(a==0):
    print("You are entering a zero age")
    print("Please enter a valid age")

else:
    print("You are below the age of consent")

print(".")
print(".")
print("End of the program")