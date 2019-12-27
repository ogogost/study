def number_of_days(month_number):
    if month_number == 1:
        return 28
    else:
        if month_number < 7: # jan - jul
            return 30 if month_number % 2 == 1 else 31
        else: # aug - dec
            return 31 if month_number % 2 == 1 else 30

print(number_of_days(12))

weather = dict()
months = [ 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
for i in range(len(months)):
    current_month = months[i]
    weather[months[i]] = [0] * number_of_days(i)

print(weather)


with open('data_one_year.txt', 'r') as data:
    #data.readline()
    for month in months:
        current_days = weather[month]
        for i in range(len(current_days)):
            current_days[i] = int(data.readline())

print(weather['apr'][23])

def process_average

while True:
    try:
        user_input = input().split()
        command = user_input[0]

            if command == 'temp':
                month = user_input[1]
                day = int(user_input[2])
                print(weather[month][day])

            # elif command == 'average':
            #     month_of_command = str(user_input[1])
            #     print(sum(weather[month_of_command] / number_of_days())

    except.IndexError:
        print('Error of index')
    except.WindowsError:
        pass