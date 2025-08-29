import random

def randNums():

    defaultArray = []

    for x in range(100):
        defaultArray.append(x)

    for y in range(20):
        dafaultArray[y] = random.randint(1, 100)
    
    for z in range(len(defaultArray)):
        if (defaultArray % 2) == 0:
            print("Even Number Found: {z}")
        else:
            print("Odd Number Found: {z}")
    

