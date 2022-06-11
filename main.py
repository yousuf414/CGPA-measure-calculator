print("------------------ CGPA CALCULATOR FOR DIU --------------------")
n = int(input("How many courses you have taken: "))
i = 1
result = 0
credits = 0
while i <= n:
    name = str(input("Enter The Course name: "))
    grade = float(input("Enter your earning grade point of the course: "))
    credit = float(input("Enter credit per hour of this course: "))
    grades = grade*credit
    result = result + grades
    credits = credits + credit
    i = i+1
print("--------------------- Your Is Result Coming ------------------------")
print("total grades:", result)
print("total credits:", credits)
sgpa = result/credits
print("SGPA of the Semester: ","{:.2f}".format(sgpa))

if sgpa == 4.00:
    print("Your Grade is A+")
    print("Your Obtaining Marks 80 to 100")
    print("Your Result is Outstanding")
elif sgpa <4.00 and sgpa >= 3.75:
    print("Your Grade is A")
    print("Your Obtaining Marks 75 to 79")
    print("Your Result is Excellent")
elif sgpa <3.75 and sgpa >= 3.5:
    print("Your Grade is A-")
    print("Your Obtaining Marks 70 to 74")
    print("Your Result is Very Good")
elif sgpa <3.5 and sgpa >= 3.25:
    print("Your Grade is B+")
    print("Your Obtaining Marks 65 to 69")
    print("Your Result is Good")
elif sgpa <3.25 and sgpa >= 3.00:
    print("Your Grade is B")
    print("Your Obtaining Marks 60 to 64")
    print("Your Result is Satisfactory")
elif sgpa <3.00 and sgpa >= 2.75:
    print("Your Grade is B-")
    print("Your Obtaining Marks 55 to 59")
    print("Your Result is Above Average")
elif sgpa <2.75 and sgpa >= 2.5:
    print("Your Grade is C+")
    print("Your Obtaining Marks 50 to 49")
    print("Your Result is Average")
elif sgpa <2.5 and sgpa >= 2.25:
    print("Your Grade is C")
    print("Your Obtaining Marks 45 to 49")
    print("Your Result is Bellow Average")
elif sgpa <2.25 and sgpa >= 2.00:
    print("Your Grade is D")
    print("Your Obtaining Marks 40 to 44")
    print("Your Result is Pass")
else:
    print("Fail\nYour Obtaining Marks below 39\nBetter Luck Next time!")
    

