# Lesson 5 - a function that returns functions
from datetime import datetime


def calculate(kind='+', *args):
    result = 0
    if kind == '+':
        for a in args:
            result += a
    elif kind == '-':
        for a in args:
            result -= a
    return result


print(calculate('+', 1, 2, 3))
print(calculate('-', 1, 2, 3))


def create_function(kind='+'):
    source = '''
def f(*args):
    result = 0
    for a in args:
         result {}= a
    return result
    '''.format(kind)
    exec(source, globals())
    return f


f_add = create_function('+')
print(f_add(1, 2, 3, 4))
f_subs = create_function('-')
print(f_subs(1, 2, 3, 4))
print('-' * 30)
# LAB


def time_span_m(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 60)[0]


def time_span_h(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 3600)[0]


def time_span_d(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 86400)[0]


start = datetime(1992, 1, 13, 0, 0, 0)
end = datetime.now()

print(time_span_m(start, end))
print(time_span_h(start, end))
print(time_span_d(start, end))

print('-' * 30)


def create_function(span):
    sec = 0

    if span == 'm':
        sec = 60
    elif span == 'h':
        sec = 3600
    elif span == 'd':
        sec = 86400

    source = '''
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]   
    '''.format(sec)
    exec(source, globals())
    return f


f_minutes = create_function('m')
print('It passed {} minutes since I was born.'.format(f_minutes(start, end)))
f_hours = create_function('h')
print('It passed {} hours since I was born.'.format(f_hours(start, end)))
f_days = create_function('d')
print('It passed {} days since I was born.'.format(f_days(start, end)))
