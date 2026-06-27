a = input("Enter the number: ")
print(f"Mulplication table of {a}: is ")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid input!")

print("some lines of code")
print("End of the program")