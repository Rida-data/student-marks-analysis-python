# Student Marks Data Analysis
# My second Python project

from statistics import median

marks = [78, 85, 62, 90, 56, 73, 88, 45, 69, 94]

average = sum(marks) / len(marks)
middle_mark = median(marks)
highest = max(marks)
lowest = min(marks)

passed = sum(1 for mark in marks if mark >= 40)
failed = sum(1 for mark in marks if mark < 40)
pass_rate = (passed / len(marks)) * 100

print("Student Marks:", marks)
print("\n--- Student Marks Summary ---")
print("Total Students:", len(marks))
print("Average Mark:", average)
print("Median Mark:", middle_mark)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Students Passed:", passed)
print("Students Below Passing Mark:", failed)
print("Pass Rate:", pass_rate, "%")

