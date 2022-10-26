def countNoDigits(number):
    if number//10 == 0:
        return 1
    return 1 + countNoDigits(number//10)


n = 345289467
print("Number of digits : % d" % (countNoDigits(n)))

