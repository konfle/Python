# Lesson 2 - Special arguments args and kwargs


def BuyMe(prefix='Please buy me', what='something nice', *args, **kwargs):
    print(prefix, what)
    print(args)
    print(kwargs)


BuyMe('Please buy me', 'a new car', 'a cat', 'a dog', 'a dragon', shop='market', color='any')

products = ['milk', 'bread', 'flakes']
parameters = {'price': 'low', 'time': 'now'}

BuyMe('Buy me', 'newspaper', *products, **parameters)

# LAB


def calculate_paint(efficiency_ltr_per_m2, *args):
    summary = 0
    area = 0
    for room_m2 in args:
        needed_amount_of_paint = room_m2 * efficiency_ltr_per_m2
        summary += needed_amount_of_paint
        area += room_m2
    return 'To paint your area {} you need {} liters of paint'.format(area, summary)


client_no1 = calculate_paint(0.5, 20, 15)
print(client_no1)

areas_to_calculate = (20, 15)
client_no2 = calculate_paint(0.5, *areas_to_calculate)
print(client_no2)


def log_it(*args):
    path = r'C:\Users\Domowy\Desktop\Python\Intermediate\Functions\log_it.txt'
    log_file = open(path, 'a')
    for words in args:
        log_file.write(words)
        log_file.write(' ')
    log_file.write('\n')
    log_file.close()


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')
