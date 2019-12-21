import random

print(random.randint(1, 100))

while True:

    a = random.randint(0, 50)
    b = random.randint(0, 50)
    c = random.randint(0, 50)

    if a > b and a > c:
        print('A is max', a)
    if b > a and b > c:
        print('B is max', b)
    if c > b and c > a:
        print('C is max', c)
    if a == 0 or b == 0 or c == 0:
        print('A=',a)
        print('B=',b)
        print('C=',c)
        break