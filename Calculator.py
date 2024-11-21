import math
# Function to calculate the required value based on the given marks
def calculate_value(marks):
    # Sort the marks in descending order and take the top 3
    top_3_marks = sorted(marks, reverse=True)[:3]

    # Calculate the average of the top 3 marks
    average = sum(top_3_marks) / len(top_3_marks)

    # Perform the required calculations
    result = (70 - (average * 0.30)) / 0.7

    rounded_result = math.ceil(result)

    return rounded_result


# Ask the user for 4 marks
marks = []
print("Enter the Mark for Level 5 across your four modules:\n")
for i in range(4):
    mark = float(input(f"Enter mark {i + 1}: "))
    marks.append(mark)

# Calculate the result and print it
result = calculate_value(marks)
print(f"What you'll need to get on your modules this year to secure a 1st honours: {result}")
