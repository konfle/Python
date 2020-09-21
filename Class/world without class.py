car_01 = {
    'car_brand': 'Seat',
    'car_model': 'Ibiza',
    'car_is_air_bag_ok': 'True',
    'car_is_painting_ok': 'True',
    'car_is_mechanic_ok': 'True',
}
car_02 = {
    'car_brand': 'Opel',
    'car_model': 'Corsa',
    'car_is_air_bag_ok': 'True',
    'car_is_painting_ok': 'False',
    'car_is_mechanic_ok': 'True',
}


def is_car_damaged(a_car):
    return not (a_car['car_is_air_bag_ok'] and a_car['car_is_painting_ok'] and a_car['car_is_mechanic_ok'])


print(is_car_damaged(car_01))
print(is_car_damaged(car_02))

cars = [car_01, car_02]

for c in cars:
    print("{} {} damaged = {}".format(c['car_brand'], c['car_model'], is_car_damaged(c)))

# LAB
cake_01 = {
    'cake_taste': 'vanilia',
    'cake_glaze': 'chocolade',
    'cake_text': 'Happy Brithday',
    'cake_weight': '0.7',
}
cake_02 = {
    'cake_taste': 'tee',
    'cake_glaze': 'lemon',
    'cake_text': 'Happy Python Coding',
    'cake_weight': '1.3',
}


def show_cake_info(a_cake):
    return ('{} cake with {} glaze with text "{}" of {} kg'.format(
        a_cake['cake_taste'], a_cake['cake_glaze'], a_cake['cake_text'], a_cake['cake_weight']))


# show_cake_info(cake_01_taste, cake_01_glaze, cake_01_text, cake_01_weight)
# show_cake_info(cake_02_taste, cake_02_glaze, cake_02_text, cake_02_weight)

cake_list = [cake_01, cake_02]
for cake in cake_list:
    print(show_cake_info(cake))
