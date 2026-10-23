
# Student Marks Data Analysis
# BSc Statistics and Mathematics Portfolio Project

from statistics import mean, median, stdev

marks = [78, 85, 62, 90, 56, 73, 88, 45, 69, 94]

# Calculate descriptive statistics
average = mean(marks)
middle_mark = median(marks)
highest = max(marks)
lowest = min(marks)
data_range = highest - lowest
data_variance = stdev(marks) ** 2
data_stdev = stdev(marks)

# Calculate pass statistics (pass mark: 40)
passed = sum(1 for mark in marks if mark >= 40)
failed = sum(1 for mark in marks if mark < 40)
pass_rate = (passed / len(marks)) * 100

# Display results
print("STUDENT MARKS DATA ANALYSIS")
print("-" * 30)
print("Marks:", marks)
print("Total Students:", len(marks))
print("Mean:", average)
print("Median:", middle_mark)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Range:", data_range)
print("Sample Variance:", data_variance)
print("Sample Standard Deviation:", data_stdev)
print("Students Passed:", passed)
print("Students Below Passing Mark:", failed)
print("Pass Rate:", pass_rate, "%")
