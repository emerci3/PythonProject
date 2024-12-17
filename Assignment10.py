#Display the values

Age=float(input("How old are you?:"))

# Classify

if Age<18:
    print ("User is a minor")
elif 18<= Age< 65:
    print ("User is an Adult")
elif Age> 65:
    print ("User is a Senior citizen")

#Validate

if Age<0:
    print ("Enter an age greater than 0:")