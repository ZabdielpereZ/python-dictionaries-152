from helper import d 

# removing key-value pairs from dictionary

student_grades = {
    "Alice" : 85,
    "Bob" : 90,
    "Charlie" : 78
}

# using .pop() : removes the specified key and return its value. If the key doesn't exist it will return a default value that we specify
# bob_grade = student_grades.pop("Bob", "Not found")
# print(bob_grade)
# print(student_grades)

d()

# using .popitem() removes and returns the last key-value pair as a tuple 
last_item = student_grades.pop.item()
print(last_item)
print(student_grades)

d()

# using del 
# delete the key-value pair from the dictionary, with no return value 
del student_grades["Charlie"]
print(student_grades)

# using .clear() : removes all key-value pairs from the dictionary, leaving it empty
student_grades.clear()
print(student_grades)