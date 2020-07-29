# Lesson 2 - generators
listA = list(range(6))
listB = list(range(6))

print(listA, listB)

product = []

for a in listA:
    for b in listB:
        product.append((a, b))

print(product)

product = [(a, b) for a in listA for b in listB]
print(product)

product = [(a, b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0]
print(product)

product = {a: b for a in listA for b in listB if a % 2 == 1 and b % 2 == 0}
print(product)

gen = ((a, b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)
print(gen)

print(next(gen))
print(next(gen))
print('-' * 30)
for x in gen:
    print(x)
print('-'*30)
for x in gen:
    print(x)

print('*' * 30)
gen = ((a, b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)
while True:
    try:
        print(next(gen))
    except StopIteration:
        print('all values have been generated')
    break

# LAB
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

everyone_with_everyone = ((start, end) for start in ports for end in ports)
counter = 0
while True:
    try:
        print(next(everyone_with_everyone))
        counter += 1
    except StopIteration:
        print('All values have been generated\n You generated {} values'.format(counter))
        break


everyone_with_everyone = ((start, end) for start in ports for end in ports if start != end)
counter = 0
while True:
    try:
        print(next(everyone_with_everyone))
        counter += 1
    except StopIteration:
        print('All values have been generated\n You generated {} values'.format(counter))
        break

everyone_with_everyone = ((start, end) for start in ports for end in ports if start < end)
counter = 0
while True:
    try:
        print(next(everyone_with_everyone))
        counter += 1
    except StopIteration:
        print('All values have been generated\n You generated {} values'.format(counter))
        break
