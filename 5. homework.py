def short_name (first_name, last_name, family_name):
    return last_name + " " + first_name[0] +". " + family_name[0] + ". "

print(short_name("Ivan", "Ivanov", "Ivanovich"))

# def is_sorted(data):
#     ordered = is_sorted(data)
#     if ordered == data:
#         return True
#     ordered.reverse()
#     if ordered == data:
#         return True
#     return False
#
#
# data = [1, 2, 3]
# print(is_sorted(data))
# data.reverse(data)
# print(is_sorted(data))
# data[0] = 0
# print(is_sorted(data))


def distinct(data):
    # elements = set()
    # for value in data:
    #     elements.add(value)
    data[0] = 12
    return list(set(data))

values = [1, 2, 3, 3]
print(distinct(values))
print(values)
print(distinct([1, 2, 2, 3, 3, 3, 3]))

def form_map(names, phones):
    name_to_phone = dict()
    for i in range(len(names)):
        name_to_phone[names[i]] = phones[i]
    return name_to_phone

names = ["Ivan", "Olga"]
phones = ["12-32-23", "32-43-54"]

print(form_map(names, phones))

# 12.04.2019
def format_date(date):
    parts = date.split(".")
    changed_month = months.get(int(parts[1]))
    if changed_month is None:
        return "Error during passin"
    else:
        return parts[0] + " " + changed_month + " " + parts[2]

print(format_date('12.14.2019'))