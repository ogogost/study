class Car:
    # model = ''
    # color = ''
    # horses = 0
    #
    def __init__(self, model, color='', horses=0, velocity = 0):
        self.model = model
        self.color = color
        self.horses = horses
        self.velocity = velocity

    def speedUp(self, vel):
        self.velocity += vel

    def __str__(self):
        return self.model + " " + self.color



bmw = Car('BMW', 'Red', 300)

bmw.strange_field = 'hello'
bmw.break_car = lambda : print('car is broken')

# bmw.model = "BMW"
# bmw.color = 'black'
# bmw.horses = 300
bmw.speedUp(10)
print(bmw.velocity)
bmw.break_car()

audi = Car("Audi", "red", 234)
# audi.model = "Audi"
# audi.color = 'red'
# audi.horses = 2324

print(bmw.model, audi.model)
print(bmw.color, audi.color)

str_bmw = str(bmw)
print(bmw)
print(bmw.__dict__)

print(type(bmw))