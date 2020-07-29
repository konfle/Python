# Lesson 3 - Function eval()
import math
'''
var_x = 10
password = "My super secret password"

source = '__import__("os").getcwd()'

# globals = globals().copy()
# del globals['password']
globals = {}
result = eval(source, globals)
print(result)

# print(globals())
'''
# LAB
argument_list = []
for i in range(0, 100, 1):
    argument_list.append(i/10)

# try: 2*x, math.sin(x), 3*x**2+2*x-4
print('Use x to mark formula argument\n Give a mathematical formula: ')
formula = input()

for x in argument_list:
    print(eval(formula))
