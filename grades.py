print("Enter marks for 5 subjects:")

marks = []

for i in range(5):
    mark = float(input(f"Subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
average = total / 5

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\nMarks for each subject:")
for i in range(5):
    print(f"Subject {i+1}: {marks[i]}")

print(f"\nAverage Marks: {average:.2f}")
print(f"Grade: {grade}")
