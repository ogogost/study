


class BankClient():
    min_life = 15 * 12
    def __init__(self, name, age, inc, status):
        self.name = name
        self.age = age
        self.inc = inc
        self.status = status

    def get_month_inc(self):
        return self.inc / 12

    def accept_credit(self, value):
        pay_time = 70 - self.age
        if (self.inc - value / pay_time - self.min_life > 0) and (pay_time > 0):
            return True
        else:
            return False



max = BankClient("Max", 99, 1000, "investor")

print(max.age)
print(max.get_month_inc())

print(max.accept_credit(1000))

class cat():
    def __init__(self, name, color, weight, age):
        self.name = name
        self.color = color
        self.weight = weight
        self.age = age

    def meow(self):
        return self.name + ' says meowwwwwww'

    def is_healty(self):
        if self.age < self.weight:
            return True
        else:
            return False

barsik = cat("barsik", 'black', 7, 2)

print(barsik.is_healty())
print(barsik.color)
print(barsik.meow())

class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('Приятного аппетита!')

    def getName(self):
        return self.name

    def setName(self):
        self.name = self

    def makeNoise(self):
        print(self.name, ' говорит грррр')

cat = Animal('Tima')

print(cat.getName())
cat.makeNoise()
cat.eat()
