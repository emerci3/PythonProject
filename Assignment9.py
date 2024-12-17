

#Display the values

Character= input("Enter an alphabet:")

# Determine if a vowel or consonant

if len(Character) !=1:
 print(" Enter a single alphabet:")

# Validate
vowels="aeiouYAEIOUY"

if Character in vowels:
    print(" character is a vowel")
else:
    print (" character is a consonant")

