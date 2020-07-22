# Lesson 1 - variables, the id () function and the is operator

myvar = 'Hello Pycharm'
myvar2 = myvar + "-"
print(myvar2)
print(type(myvar), type(myvar))
print('Is value the same?', myvar == myvar2)
print('Are the variables the same?', myvar is myvar2)
print(id(myvar), id(myvar2))
myvar2 = myvar2[:-1]
print(type(myvar), type(myvar))
print('Is value the same?', myvar == myvar2)
print('Are the variables the same?', myvar is myvar2)
print(id(myvar), id(myvar2))

# LAB

a = b = c = 20
print('There are values of variables a:{}, b:{}, c:{}'.format(a, b, c))
print('There are id of variables a:{}, b:{}, c:{}'.format(id(a), id(b), id(c)))
a = b = c = [1, 2, 3, 4]
print('There are values of variables a:{}, b:{}, c:{}'.format(a, b, c))
print('There are id of variables a:{}, b:{}, c:{}'.format(id(a), id(b), id(c)))
x = 10
y = 10 + 1234567890 - 1234567890
print(id(x), id(y))
