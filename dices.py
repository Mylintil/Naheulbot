def roll(number, type):
    import random
    max = 20
    if(type == "D20"):
        max = 20
    if(type == "D6"):
        max = 6

    res = 0
    for i in range(number):
        res = res + random.randint(1, max)

    return res
