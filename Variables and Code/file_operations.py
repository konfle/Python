# Lesson 4 - File operations in logical expressions
import os

path = r'e:\tut.txt'

# os.remove(path)

if os.path.isfile(path):
    print("File %s exist" % path)
else:
    print("Crating a file %s" % path)
    open(path, 'x').close()
    print('File %s created' % path)

result = os.path.isfile(path) or open(path, 'x').close()
print(result)

# LAB

path = r'e:\tut.txt'


# os.remove(path)


def words_counter(path_to_file):
    file = open(path_to_file)
    words = file.read()
    count = words.split()
    return len(count)


if os.path.isfile(path):
    number_of_words = words_counter(path)
    print('Number of words in file: {}'.format(number_of_words))
    print('Number of words in file: %s' % number_of_words)
else:
    print('Sorry file doesnt exist.')

result = os.path.isfile(path) and words_counter(path)
print(result)
