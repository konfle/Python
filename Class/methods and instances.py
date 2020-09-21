class Car:

    def __init__(self, brand, model, is_air_bag_ok, is_painting_ok, is_mechanic_ok):
        self.brand = brand
        self.model = model
        self.is_air_bag_ok = is_air_bag_ok
        self.is_painting_ok = is_painting_ok
        self.is_mechanic_ok = is_mechanic_ok

    def is_damaged(self):
        return not (self.is_air_bag_ok and self.is_painting_ok and self.is_mechanic_ok)

    def get_info(self):
        print("{} {}".format(self.brand, self.model.upper()))
        print('Air Bag  - ok -   {}'.format(self.is_air_bag_ok))
        print('Painting - ok -   {}'.format(self.is_painting_ok))
        print('Mechanic - ok -   {}'.format(self.is_mechanic_ok))
        print('-' * 20)


car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)

car_01.get_info()
car_02.get_info()

print(car_01.brand, car_01.model, car_01.is_damaged())
print(car_02.brand, car_02.model, car_02.is_damaged())

print(car_01.brand, car_01.model, car_01.is_air_bag_ok, car_01.is_painting_ok, car_01.is_mechanic_ok)
print(car_02.brand, car_02.model, car_02.is_air_bag_ok, car_02.is_painting_ok, car_02.is_mechanic_ok)

'''
def is_car_damaged(a_car):
    return not (a_car['car_is_air_bag_ok'] and a_car['car_is_painting_ok'] and a_car['car_is_mechanic_ok'])


print(is_car_damaged(car_01))
print(is_car_damaged(car_02))

cars = [car_01, car_02]

for c in cars:
    print("{} {} damaged = {}".format(c['car_brand'], c['car_model'], is_car_damaged(c)))
'''

# LAB


class Cake:

    def __init__(self, product_name, kind, taste, additives, filling):
        self.product_name = product_name
        self.kind = kind
        self.taste = taste
        self.addictions = additives.copy()
        self.filling = filling

    def show_info(self):
        print('{}'.format(self.product_name.upper()))
        print('Kind: {}'.format(self.kind))
        print('Taste: {}'.format(self.taste))
        if len(self.addictions) > 0:
            print('Addictions:')
            for add in self.addictions:
                print("\t{}".format(add))
        if len(self.filling) > 0:
            print('Filling: {}'.format(self.filling))
        print('--' * 10)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, add_list):
        for add in add_list:
            self.addictions.append(add)


cake1 = Cake('Chocolate', 'cookies', 'sweet choco', ['white chocolate', 'peanuts'], 'toffee')
cake2 = Cake('Vanilla', 'cake', 'sweet vanilla', ['chocolate', 'strawberry'], 'chocolate sauce')
cake3 = Cake('Salt Carmel', 'muffin', 'salt', ['whipped cream'], '')

bake_offer = [cake1, cake2, cake3]

print('*' * 20)
print('\n')
print('--- START TESTS ---')

# Tests for method show_info
print('Test results for method show_info:')
cake1.show_info()
cake2.show_info()
cake3.show_info()

# Test for method set_filling
print('Test results for method set_filling:')
cake1.set_filling('apple sauce')
print(cake1.filling)

# Test for method add_additives
print('Test result for method add_additives:')
cake3.add_additives(['cocoa powder', 'coconuts'])
print(cake3.addictions)

print('--- END OF TESTS ---\n')

print('Today in our offer:')
for cake in bake_offer:
    cake.show_info()
