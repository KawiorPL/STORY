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

print(f"list {list}")
print(f"max is: {maxFun(list)}")