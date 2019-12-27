data = [1, 2, 3]
# print(data[3])

# try:
#     # a = int(input())
#     # b = int(input())
#     # print(a + b)
# except ValueError as error:
#     print("Wrong")
#     print(error)
# finally:
#     print('finally')
# try:
#     file = open('test.txt', 'r')
# # print(file.readline())
#     for line in file:
#         print(line)
# except:
#     print("error")
# finally:
#     if file is not None:
#         print('file closed')
#         file.close()

with open('test.txt', 'r') as file:
    for line in file:
        print(line, end='')

