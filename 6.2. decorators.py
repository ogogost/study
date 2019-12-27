import time

def run_with_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print(end_time - start_time)

def action():
    return [i for i in range(100000)]

# start_time = time.time()
# action()
# end_time = time.time()
# print(end_time - start_time)

run_with_time(action)