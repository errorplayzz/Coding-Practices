# Using break
for i in range(100):
    if i == 35:
        print("Found 35")
        break
    print(i)

print("Loop ended")


#using continue
for i in range(50):
    if i ==25:
        print("Found 25")
        continue
    print(i)

print("Loop ended")

#using pass
print("Using pass")
for i in range(50):
    pass

i = 0
while(i<50):
    print(i)
    i += 1