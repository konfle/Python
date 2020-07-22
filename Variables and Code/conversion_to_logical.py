# Lesson 3 - Automatic conversion to logical type

listOfErrors = [101, 102, 100]
print('Variable listOfErrors:', listOfErrors, type(listOfErrors))
if len(listOfErrors) > 0:
    print('TRUE')

# LAB

options = ['load data', 'export data', 'analyze & predict']
choice = 'x'


def display_options(list_of_choices):
    for i in range(len(list_of_choices)):
        print("{} - {}".format(i + 1, list_of_choices[i]))
    choice_in = input('Select option above or press enter to exit: ')
    return choice_in


while choice:
    choice = display_options(options)
    if choice:
        try:
            choice_num = int(choice) - 1
            if not choice_num < 0 and choice_num < len(options):
                print('Your choice was {} - {}'.format(choice_num + 1, options[choice_num]))
            else:
                print('Bad choice try one more time from number 1-3')
        except:
            print('You need to enter a number')
    else:
        print("THE END")
