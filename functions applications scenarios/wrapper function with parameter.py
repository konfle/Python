# Lesson 2 - wrapper function with parameter
import os
from datetime import datetime as dt


def create_function_with_wrapper_log_to_file(log_file_path):
    def create_function_with_wrapper(func):
        def func_with_wrapper(*args, **kwargs):
            file = open(log_file_path, "a")
            file.write('-' * 20 + "\n")
            file.write('Function "{}" started at {}\n'.format(func.__name__, dt.now().isoformat()))
            file.write('Following arguments ware used:\n')
            file.write(" ".join("{}".format(x) for x in args))
            file.write("\n")
            file.write(" ".join("{}={}".format(k, v) for (k, v) in kwargs.items()))
            file.write("\n")
            result = func(*args, **kwargs)
            file.write('Function returned {}\n'.format(result))
            file.close()
            return result
        return func_with_wrapper
    return create_function_with_wrapper


@create_function_with_wrapper_log_to_file(r'C:\Users\Domowy\Desktop\Python\Intermediate\functions applications scenarios\change_salary.txt')
def change_salary(emp_name, new_salary, is_bonus=False):
    print('CHANGING SALARY FOR {} TO {} AS BONUS={}'.format(emp_name, new_salary, is_bonus))
    return new_salary


@create_function_with_wrapper_log_to_file(r'C:\Users\Domowy\Desktop\Python\Intermediate\functions applications scenarios\change_position.txt')
def change_position(emp_name, new_position):
    print('CHANGING POSITION FOR {} TO {}'.format(emp_name, new_position))
    return new_position


print(change_salary('Johnson', 20000, True))
print(change_salary('Johnson', 20000, is_bonus=True))
print(change_position('Johnson', 'CEO'))
print(change_position('Jefferson', 'Creative Director'))
print('-' * 10, ' LAB ', '-' * 10)
# LAB


def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            file = open(log_file_path, "a")
            file.write('Action {} executed on {} on {}'.format(logged_action, path, dt.now().strftime("%Y-%m-%d %H:%M:%S \n")))
            file.close()
            result = func(path)
            return result
        return the_real_wrapper
    return wrapper_with_log_to_known_file


@wrapper_with_log_file('FILE_CREATE', r'C:\Users\Domowy\Desktop\Python\Intermediate\functions applications scenarios\dummy_file.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")


@wrapper_with_log_file('FILE_DELETE', r'C:\Users\Domowy\Desktop\Python\Intermediate\functions applications scenarios\dummy_file.txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'C:\Users\Domowy\Desktop\Python\Intermediate\functions applications scenarios\dummy_file.txt')
delete_file(r'C:\Users\Domowy\Desktop\Python\Intermediate\functions applications scenarios\dummy_file.txt')
create_file(r'C:\Users\Domowy\Desktop\Python\Intermediate\functions applications scenarios\dummy_file.txt')
delete_file(r'C:\Users\Domowy\Desktop\Python\Intermediate\functions applications scenarios\dummy_file.txt')
