N = 10
data = [0 for i in range(N)]
count_zero = 0

def park(n):
    for i in range(N):
        if data.count(0) == 0:
            print('No free')
            break

        if data[i] != 0:
            data.insert(n, i)

    print(data)

def leave(n):
    data.remove(n)
    print(data)

def free():
   print(data.count(0))

def show():
    print(data)

while True:
    com = ''
    com = input('Input command:').split()
    if com == 'park':
        park(n)
    elif com == 'leave':
        leave(n)
    elif com == 'free':
        free()
    elif com == 'show':
        show()
