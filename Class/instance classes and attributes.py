class Car:

    def __init__(self, brand, model, is_air_bag_ok, is_painting_ok, is_mechanic_ok):
        self.brand = brand
        self.model = model
        self.is_air_bag_ok = is_air_bag_ok
        self.is_painting_ok = is_painting_ok
        self.is_mechanic_ok = is_mechanic_ok


car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)

'''
def is_car_damaged(a_car):
    return not (a_car['car_is_air_bag_ok'] and a_car['car_is_painting_ok'] and a_car['car_is_mechanic_ok'])


print(is_car_damaged(car_01))
print(is_car_damaged(car_02))

cars = [car_01, car_02]

for c in cars:
    print("{} {} damaged = {}".format(c['car_brand'], c['car_model'], is_car_damaged(c)))
'''

print(car_01.brand, car_01.model, car_01.is_air_bag_ok, car_01.is_painting_ok, car_01.is_mechanic_ok)
print(car_02.brand, car_02.model, car_02.is_air_bag_ok, car_02.is_painting_ok, car_02.is_mechanic_ok)

# LAB


class Cake:

    def __init__(self, product_name, kind, taste, additives, filling):
        self.product_name = product_name
        self.kind = kind
        self.taste = taste
        self.addictions = additives.copy()
        self.filling = filling


cake1 = Cake('Chocolate', 'cookies', 'sweet choco', ['white chocolate', 'peanuts'], 'toffee')
cake2 = Cake('Vanilla', 'cake', 'sweet vanilla', ['chocolate', 'strawberry'], 'chocolate sauce')

bake_offer = [cake1, cake2]

print('_' * 20)
print('Today in our offer:')
for cake in bake_offer:
    print('{} - ({}) main taste: {} with additives of {}, filled with {}'.format(cake.product_name, cake.kind, cake.taste, cake.addictions, cake.filling))
