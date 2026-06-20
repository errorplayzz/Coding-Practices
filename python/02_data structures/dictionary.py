marks = {
    "error": 98,
    "sameer": 99,
    "arry": 100
}

print(type(marks), marks)

print(marks["error"])

print("methods of dictionary")

another_marks = {
    "error": 98,
    "sameer": 99,
    "arry": 100,
    0: "zero",
}

# print(another_marks.items())
# print(another_marks.keys())

# another_marks.update({"arry": 98})

print(another_marks.get("aarry")) 
print(another_marks.get("arry")) 

print(another_marks)



