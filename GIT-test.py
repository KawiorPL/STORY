import random

list=[]


def maxFun(list):
    max=0
    for i in list:
        if i > max:
            max =i
        else:
            continue
    return max




for i in range(10):
    x=random.randint(1,100)
    list.append(x)
    print(x)

z=maxFun(list)
print(f"list {list}")
print(f"max is: {z}")

y=random.randint(75,100)

if y - z>0:
    print(f"You win = Your number {y} and my number {z}!!!")
else:
    print(f"I win Your number {y} and my number {z}!!!")