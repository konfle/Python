# Lesson 1 - wrapper for functions and decorators
import datetime
import functools


def create_function_with_wrapper(func):
    def func_with_wrapper(*args, **kwargs):
        print('Function "{}" started at {}'.format(func.__name__, datetime.datetime.now().isoformat()))
        print('Following arguments ware used:')
        print(args, kwargs)
        result = func(*args, **kwargs)
        print('Function returned {}'.format(result))
        return result
    return func_with_wrapper


@create_function_with_wrapper
def change_salary(emp_name, new_salary, is_bonus = False):
    print('CHANGING SALARY FOR {} TO {} AS BONUS={}'.format(emp_name, new_salary, is_bonus))
    return new_salary


print(change_salary('Johanson', 20000, True))

# change_salary = create_function_with_wrapper(change_salary)

print(change_salary('Johnson', 20000, is_bonus=True))

# LAB


def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


print(get_sequence(18))


def wrapper_time(a_function):
    def a_wrapped_function(*args, **kwargs):
        time_start = datetime.datetime.now()
        v = a_function(*args, **kwargs)
        time_stop = datetime.datetime.now()
        print('Function {} was done in {} '.format(a_function.__name__, time_stop - time_start))
        return v
    return a_wrapped_function


wrapper_get_sequence = wrapper_time(get_sequence)

print(wrapper_get_sequence(18))

# LAB with decorator - like infinity loop

'''
def wrapper_time(a_function):
    def a_wrapped_function(*args, **kwargs):
        time_start = datetime.datetime.now()
        v = a_function(*args, **kwargs)
        time_stop = datetime.datetime.now()
        print('Function {} was done in {} '.format(a_function.__name__, time_stop - time_start))
        return v
    return a_wrapped_function


@wrapper_time
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


print(get_sequence(18))
'''
