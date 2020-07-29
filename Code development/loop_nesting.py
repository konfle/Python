# Lesson 1 - Loop nesting, and the same thing in single-line form
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

product = [(a, b) for a in listA for b in listB if a % 2 ==1 and b % 2 == 0]
print(product)

product = {a: b for a in listA for b in listB if a % 2 ==1 and b % 2 == 0}
print(product)

# LAB
ports_start = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
ports_end = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

everyone_with_everyone = [(start, end) for start in ports_start for end in ports_end]
print(everyone_with_everyone)
print(len(everyone_with_everyone))

everyone_with_everyone = [(start, end) for start in ports_start for end in ports_end if start != end]
print(everyone_with_everyone)
print(len(everyone_with_everyone))

everyone_with_everyone = [(start, end) for start in ports_start for end in ports_end if start < end]
print(everyone_with_everyone)
print(len(everyone_with_everyone))
