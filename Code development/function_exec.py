# Lesson 4 - function exec()
import os.path
var_x = 10

source ='''
new_var = 1
for i in range(var_x):
    print('-' * i)
    new_var += i
'''

result = exec(source)
print(result)

print(var_x)
print(new_var)

source = input("Enter your expression: ")
print(eval(source))


# LAB
files_to_process = [
    r"C:\Users\Domowy\PycharmProjects\udemy_python_intermediate\code_development\exec_script_1.py",
    r"C:\Users\Domowy\PycharmProjects\udemy_python_intermediate\code_development\exec_script_2.py"
    ]

for file_path in files_to_process:

    with open(file_path, 'r') as f:
        print(os.path.basename(file_path))
        source = f.read()
        exec(source)


