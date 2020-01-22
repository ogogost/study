# data = [1, 2, 3]
# data.remove(3)
# for i in data:
#     if data[i] == 2:
#         data.remove(i)
# print(data)

class Test:

    def __init__(self, id):
        self.id = id

x = Test()
print(x)

data = []
for i in range(3):
    data.append(Test(i))

print(data)

