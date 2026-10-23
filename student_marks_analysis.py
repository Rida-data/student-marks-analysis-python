
# Student Marks Data Analysis
# My second Python project

marks = [78, 85, 62, 90, 56, 73, 88, 45, 69, 94]

print("Student Marks:", marks)

average = sum(marks) / len(marks)

print("Average Mark:", average)

highest = max(marks)
lowest = min(marks)

print("Highest Mark:", highest)
print("Lowest Mark:", lowest)

passed = sum(1 for mark in marks if mark >= 40)
pass_rate = (passed / len(marks)) * 100

print("Students Passed:", passed)
print("Pass Rate:", pass_rate, "%")

failed = sum(1 for mark in marks if mark < 40)

print("Students Below Passing Mark:", failed)

print("\n--- Student Marks Summary ---")
print("Total Students:", len(marks))
print("Average Mark:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Students Passed:", passed)
print("Students Below Passing Mark:", failed)
print("Pass Rate:", pass_rate, "%")
