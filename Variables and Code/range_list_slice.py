# Lesson 7 - range, list, slice

for i in range(10, 0, -1):
    print(i)

list = list(range(10))
print('List:', list, type(list), id(list))
list2 = list[:]
print('List:', list2, type(list2), id(list2))
print(list[-1::-1])

# LAB

colors = ["red", "orange", "green", "violet", "blue", "yellow"]


def colors_to_use(list_of_colors, amount_of_colors):
    try:
        col = list_of_colors[:]
        aoc = amount_of_colors
        return col[:aoc]
    except:
        print('Something went wrong!')


for i in range(1, len(colors)+1):
    print(colors_to_use(colors, i))

corporation_definition = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod ' \
                   'przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem ' \
                   'realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy'\
                   ' do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli.'

print(corporation_definition[corporation_definition.find('z'):corporation_definition.find(';')])
