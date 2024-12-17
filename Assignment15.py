

import math

#Create a function is_prime
def is_prime(n):
    #Handling numbers if its 1 or less than that
    if n <=1:
        return False
    if n <=3:
        return True

    # Handle even numbers and multiply by 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    #Check for factors of 5 to a sqrt (n) and skip even numbers and multiply by 3
    limit= int(math.sqrt(n)) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2)== 0:
            return False
        return True

    print(is_prime(15))
