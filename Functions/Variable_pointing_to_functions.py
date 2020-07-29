# Lesson 3 - Variable pointing to functions


def BuyMe(what):
    print('Give me', what)


BuyMe('a new car')

StealForMe = BuyMe
print(type(StealForMe))
StealForMe("a new car")


def go_left(*args):
    print('PLACEHOLDER - turning left with', *args)


def go_right(*args):
    print('PLACEHOLDER - turning right with', *args)


def go_forward(*args):
    print('PLACEHOLDER - going forward with', *args)


def go_back(*args):
    print('PLACEHOLDER - going back with', *args)


def start(*args):
    print('PLACEHOLDER - starting with', *args)


def stop(*args):
    print('PLACEHOLDER - stopping with', *args)


instructions = [start, go_forward, go_forward, go_left, go_forward, go_right, stop]
dish = 'pizza'
for instr in instructions:
    instr(dish)

# LAB
print('-' * 30)


def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


number = 8

transformations = [double, root, div2, negative]
for transform in transformations:
    tmp_return_value = transform(number)
    print(tmp_return_value)

print('*' * 30)

transformations = [root, root, div2, double]
for transform in transformations:
    tmp_return_value = transform(number)
    print(tmp_return_value)