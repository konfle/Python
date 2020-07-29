# Lesson 4 - Function as an argument of the function


def bake(what):
    print('Baking {}'.format(what))


def add(what):
    print('Adding {}'.format(what))


def mix(what):
    print('Mixing {}'.format(what))


cookbook = [(add, 'milk'), (add, 'eggs'), (add, 'flour'), (add, 'sugar'), (mix, 'ingredients'), (bake, 'cookies')]

for activity, obj in cookbook:
    activity(obj)
print('-' * 30)


def cook(activity, obj):
    activity(obj)


cook(bake, 'brownies')

for activity, obj in cookbook:
    cook(activity, obj)

# LAB


def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


x_table = list(range(11))


def generate_values(function_name, list_of_numbers):
    value_list = []
    for number in list_of_numbers:
        value_list.append(function_name(number))
    return value_list


print(generate_values(double, x_table))
print(generate_values(root, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))
