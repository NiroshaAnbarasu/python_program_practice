# Grade Classifier: Take a numerical grade (0-100) and output the letter grade (A, B, C, D, F)

print("Grade Classifier")

grade = float(input("Enter your numerical grade (0-100): "))

if grade >= 90 and  grade <= 100:
    print("Your letter grade is A")
elif grade >= 80 and grade < 90:
    print("Your letter grade is B")
elif grade >= 70 and grade < 80:
    print("Your letter grade is C")
elif grade >= 60 and grade < 70:
    print("Your letter grade is D")
elif grade >= 50 and grade < 60:
    print("Your letter grade is E")
elif grade < 50:
    print("Your letter grade is F")
else:
    print("You have entered invalid numerical grade")
