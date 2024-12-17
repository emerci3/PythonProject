


#Input display the values


Year=float(input("Enter a year:"))

# Determine if a leap year or not

if (Year % 4 ==0 and Year % 100 !=0 ) or (Year % 400==0):

    print (" year is a leap year")
else:
    print ("year is not a leap year.")