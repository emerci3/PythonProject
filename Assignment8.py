

# Input display the 3 values

Marks_English= float(input("Enter your marks for english (0-100):"))

Marks_Math= float(input("Enter your marks for math (0-100):"))

Marks_Science= float(input("Enter your marks for science (0-100):"))

if not (0 <=Marks_English <= 100):
    print ("Error english. Incorrect Values. Please enter a number between 0 and 100:")
elif not ( 0 <= Marks_Math <= 100):
    print ("Error math. Incorrect Values. Please enter a number between 0 and 100.")
elif not ( 0 <= Marks_Science <= 100):
    print ("Error science. Incorrect Values. Please enter a number between 0 and 100.")
# Calculate the average marks
else:
    Average_Marks = (Marks_English + Marks_Math + Marks_Science)/3
    print ("The average marks are", Average_Marks)

# Grade

if Average_Marks >=90:
    Grade = "A"
elif Average_Marks >=80:
    Grade= "B"
elif Average_Marks >=70:
    Grade= "C"
elif Average_Marks >=60:
    Grade= "D"
else:
    Grade= "F"

#Output
print( "The Average marks are",Grade)






