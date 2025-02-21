# Define the list
students = [("890", "ram", (95, 78, 99)), ("123", "kishan", (90, 98, 89)), ("567", "arjun", (59, 68, 100))]

# Function to sort by name
def sort_by_name(student):
    return student[1]

# Function to sort by total PCM marks
def sort_by_total_marks(student):
    return sum(student[2])

# Sort by name and display
sorted_by_name = sorted(students, key=sort_by_name)
print("Sorted by name:")
for student in sorted_by_name:
    print(student)

# Sort by total PCM marks in descending order and display
sorted_by_total_marks = sorted(students, key=sort_by_total_marks, reverse=True)
print("\nSorted by total PCM marks (descending):")
for student in sorted_by_total_marks:
    print(student)