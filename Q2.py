
# Student Marks Analysis

# Create a list of student marks
marks = [78, 35, 92, 40, 61]

# Convert list into tuple
marks_tuple = tuple(marks)

# Display list and tuple
print("List:", marks)
print("List Data Type:", type(marks))

print("Tuple:", marks_tuple)
print("Tuple Data Type:", type(marks_tuple))

# Find highest and lowest marks
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))

# Count students who scored at least 40
count = (
    (marks[0] >= 40) +
    (marks[1] >= 40) +
    (marks[2] >= 40) +
    (marks[3] >= 40) +
    (marks[4] >= 40)
)

print("Students scored at least 40:", count)

# Check whether all marks are between 0 and 100
valid_marks = (
    marks[0] >= 0 and marks[0] <= 100 and
    marks[1] >= 0 and marks[1] <= 100 and
    marks[2] >= 0 and marks[2] <= 100 and
    marks[3] >= 0 and marks[3] <= 100 and
    marks[4] >= 0 and marks[4] <= 100
)

print("All marks are valid:", valid_marks)

# Change an element in the list
marks[0] = 85
print("Modified List:", marks)

# Tuple elements cannot be changed
# marks_tuple[0] = 85
# This produces TypeError because tuples are immutable.
print("Original Tuple:", marks_tuple)
