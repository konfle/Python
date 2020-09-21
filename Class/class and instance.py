class Car:
    number_of_cars = 0
    list_of_cars = []

    def __init__(self, brand, model, is_air_bag_ok, is_painting_ok, is_mechanic_ok):
        self.brand = brand
        self.model = model
        self.is_air_bag_ok = is_air_bag_ok
        self.is_painting_ok = is_painting_ok
        self.is_mechanic_ok = is_mechanic_ok
        Car.number_of_cars += 1
        Car.list_of_cars.append(self)

    def is_damaged(self):
        return not (self.is_air_bag_ok and self.is_painting_ok and self.is_mechanic_ok)

    def get_info(self):
        print("{} {}".format(self.brand, self.model.upper()))
        print('Air Bag  - ok -   {}'.format(self.is_air_bag_ok))
        print('Painting - ok -   {}'.format(self.is_painting_ok))
        print('Mechanic - ok -   {}'.format(self.is_mechanic_ok))
        print('-' * 20)


print('Class level variables BEFORE creating instance:', Car.number_of_cars, Car.list_of_cars)

car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)

print('Class level variables AFTER creating instance:', Car.number_of_cars, Car.list_of_cars)

print('Id of class is:', id(Car))
print('Id of instances are:', id(car_01), id(car_02))

print('Check if object belongs to class:', isinstance(car_01, Car))
print('Check if object belongs to class using type:', type(car_01) is Car)
print('Check class of an object using __class__:', car_01.__class__)

print('List of instance attribute with values:', vars(car_01))
print('List of class attributes with values:', vars(Car))

print('List of instance attributes with values:', dir(car_01))
print('List of class attributes with values:', dir(Car))

print('Value taken from instance:', car_01.number_of_cars, 'Value taken from class:', Car.number_of_cars)

# LAB


class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, product_name, kind, taste, additives, filling):
        self.product_name = product_name
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = Cake.known_types[-1]
        self.taste = taste
        self.addictions = additives.copy()
        self.filling = filling
        Cake.bakery_offer.append(self)

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


cake1 = Cake('Chocolate', 'biscuit', 'sweet choco', ['white chocolate', 'peanuts'], 'toffee')
cake2 = Cake('Vanilla', 'cake', 'sweet vanilla', ['chocolate', 'strawberry'], 'chocolate sauce')
cake3 = Cake('Salt Carmel', 'muffin', 'salt', ['whipped cream'], '')
cake4 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa')

print('\n')
print('Today in our offer:')
for cake in Cake.bakery_offer:
    cake.show_info()
print('\n')

print('Checking is object cake1 is instance of Cake class with instance:', isinstance(cake1, Cake))
print('Checking is object cake 1 is instance of Cake class with type:', type(cake1) is Cake)

print('Checking info about instance cake1 with vars:', vars(cake1))
print('Checking info about instance cake1 with dir:', dir(cake1))

print('Checking info about class Cake with vars:', vars(Cake))
print('Checking info about class Cake with dir:', dir(Cake))
