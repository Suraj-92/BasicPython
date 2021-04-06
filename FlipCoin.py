from random import randint
from time import sleep

heads = 0
tails = 0
flip = int(input("How many coin tosses are you going to do?: "))

for i in range(flip):
    result = randint(0, 1)
    sleep(1)
    # print(result)
    if(result == 0):
        heads += 1
        print("Heads ",heads)
    else:
        tails +=1
        print("Tails ",tails)

print("The result are: ")
print("Heads Count", heads)
print("Tails Count", tails)