import random
n=0
list = [25,75,2,12,1]
while not list[0]<list[1]<list[2]<list[3]<list[4]:
    random.shuffle(list)
    n=n+1
    print(n)
print(list)