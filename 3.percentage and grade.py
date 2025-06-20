def calculate_grade_and_percentage():
    # Input marks for five subjects
    physics = float(input("Enter Physics marks: "))
    chemistry = float(input("Enter Chemistry marks: "))
    biology = float(input("Enter Biology marks: "))
    mathematics = float(input("Enter Mathematics marks: "))
    computer = float(input("Enter Computer marks: "))

    # Calculate total marks assuming each subject is out of 100
    total_marks = physics + chemistry + biology + mathematics + computer
    percentage = (total_marks / 500) * 100

    # Determine the grade based on the percentage
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "F"

    # Display the results
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

# Call the function to execute the program
calculate_grade_and_percentage()
