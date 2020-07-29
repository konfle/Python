# Lesson 5 - function compile()
import time
import math

source = "reportLine += 1"

reportLine = 0
start = time.time()
for i in range(100000):
    exec(source)
stop = time.time()
time_not_compiled = stop - start

start = time.time()
sourceCompiled = compile(source, 'internal variable source', 'exec')
for i in range(100000):
    exec(sourceCompiled)
stop = time.time()
time_compiled = stop - start

print(time_not_compiled)
print(time_compiled)
print(time_not_compiled / time_compiled)

# LAB
formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]
print('-' * 10, 'NOT COMPILED START', '-' * 10)

argument_list = []
for i in range(100000):
    argument_list.append(i/10)

results_list = []
for formula in formulas_list:
    print('Loop working right now with formula', formula)
    start = time.time()
    for arg in argument_list:
        x = arg
        results_list.append(eval(formula))
print('Max: {} Min: {}'.format(max(results_list), min(results_list)))
stop = time.time()
not_compiled = stop - start
print('-' * 10, 'COMPILED START', '-' * 10)

results_list = []
for formula in formulas_list:
    print('Loop working right now with formula', formula)
    start = time.time()
    compiled_formula = compile(formula, formula, 'eval')
    for arg in argument_list:
        x = arg
        results_list.append(eval(compiled_formula))
print('Max: {} Min: {}'.format(max(results_list), min(results_list)))
stop = time.time()
compiled = stop - start
print('-' * 10, 'TIME RESULTS', '-' * 10)
print('Time with compile is {}'.format(compiled))
print('Time without compile is {}'.format(not_compiled))