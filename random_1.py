import random
n=0
list = [25,75,2,12,1]
while list!= sorted(list):
    random.shuffle(list)
    n=n+1
    print(n)
print(list)
