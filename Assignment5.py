
#Display time in hours

Time_in_hours = float(input(" Enter time duration in hours:"))


if Time_in_hours < 0:
    print("Enter non-negative number")


else:

    time_in_minutes= Time_in_hours * 60
    time_in_seconds= Time_in_hours* 3600
    print ("The time in minutes is", time_in_minutes)
    print ("The time in seconds is", time_in_seconds)




