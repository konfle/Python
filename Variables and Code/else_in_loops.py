# Lesson 6 - The else command in loops
import urllib.request

instruction = ['say hello', 'say how are you', 'abort', 'ask for money', 'say thank you', 'say bye']
instructionApproved = []

for instr in instruction:
    print('Adding instruction:', instr)
    instructionApproved.append(instr)

    if instr == 'abort':
        print('Aborting!!!')
        instructionApproved.clear()
        break
else:
    print('Following actions will be take:', instructionApproved)

print('-' * 30)
instructionApproved.clear()

i = 0
while i < len(instruction):
    print('Adding instruction:', instruction[i])
    instructionApproved.append(instruction[i])

    if instruction[i] == 'abort':
        print('Aborting!!!')
        instructionApproved.clear()
        break
    i += 1
else:
    print('Following actions will be take:', instructionApproved)

# LAB

data_dir = r'e:/web/'
pages = [
    {'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},
    {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},
    {'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'}
    ]

i = 0
while i < len(pages):
    try:
        path = data_dir + pages[i]['name'] + '.html'
        print('Adding web file to path:', path)
        urllib.request.urlretrieve(pages[i]['url'], path)
        i += 1
    except:
        print("Oops something went wrong with page: {}".format(pages[i]['name']))
        break
else:
    print('Status: Success!')
