

# create a function called power
def power(base, exponent):

    #if your exponent is zero then handle it as it should return 1
    if exponent == 0:
        return 1

    #if the exponent is negative than invert the result
    if exponent < 0:
        base = 1/base
        exponent = -exponent

        #start processing
        results = 1

        while exponent >0:
            if exponent % 2 == 1: #if exponent is odd
                results *= base
            base *= base # Squaring the base
            exponent //= 2 # Halving the exponent

            return results

print(power(2,0))


