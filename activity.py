import random
import math

def randNums():

    defaultArray = []

    for x in range(100):
        defaultArray.append(x)

    for y in range(30):
        defaultArray[y] = random.randint(1, 100)
    
    for z in range(len(defaultArray)):
        if (defaultArray[z] % 2) == 0:
            print(f"Even Number Found: {defaultArray[z]}")
        else:
            print(f"Odd Number Found: {defaultArray[z]}")

    total = 0
    for num in range(len(defaultArray)):
        total += defaultArray[num]
    print(f"Total Sum: {total}")

    max = 0

    for num in range(len(defaultArray)):
        if num > max and isPrime(num):
            max = num

    print(max)

    for x in range(len(defaultArray)):
        if x == 0:
            return True
        sqrtNum = math.sqrt(x)

        if sqrtNum.is_integer():
            return True
        else:
            return False


        
        


def isPrime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    
    
    return True

randNums()