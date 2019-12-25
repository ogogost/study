def max_three_numbers(a, b, c):
    if a > b and a > c:
        return (a)
    elif b > a and b > c:
        return (b)
    elif c > a and c > b:
        return (c)


def year_v(year):
    if year % 4 == 0 and year // 100 != 0:
        return 'Yes'
    else:
        return 'No'


print(year_v(2000))
print(year_v(1000))


def c_of_triangle(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return (c)


print(c_of_triangle(12, 8))


def prost(number):
    result = True
    for i in range(2,number):
        if number % i == 0:
            result = False
            break
    return 'Yes' if result else 'No'

print(prost(9))

months = {
    1:'Январь',
    2:'Февраль',
    3:'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12:'Декабрь'
}
str_value = months.get(14)
if str_value is None:
    print('Wrong month')
else:
    print(str_value)

print(str_value)

def date_converter(date):
    if(date.split[1]) == 1:
        date.split[1] = 'январь'
        return(date)

# print(date(12.01.1999))

