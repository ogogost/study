a = [
    [1,2,3],
    [2,4,6],
    [3,6,9]
]

print(a[1][2])


n = 4
m = 5

a = []

a = [[0 for y in range(m)] for x in range(n) ]

for i in range(n):
    for j in range(m):
        a[i][j] = n * m

print(a)


for row in a:
    for element in row:
        print(element, end = ' ')
    print()


