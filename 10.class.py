import time

def run_timed(fun, *args):
    begin_time = time.time()
    fun(*args)
    end_time = time.time()
    print(end_time - begin_time)

def first():
    a = 1
    b = 2



def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


def python_sort(data):
    print(sorted(data))


import random

numbers = []
numbers_for_python = []
n = 1000
for i in range(n):
    current_number = random.randint(0, 10000000)
    numbers.append(current_number)
    numbers_for_python.append(current_number)

run_timed(bubble_sort, numbers)
run_timed(python_sort, numbers_for_python)



