#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number - (10* int(number/10))
if last > 5:
    evaluation = "greater than 5"
elif last == 0:
    evaluation = "0"
elif last != 0 and last < 6:
    evaluation = "less than 6 and not 0"
print("Last digit of {} is {} and is {}".format(number, last, evaluation))
