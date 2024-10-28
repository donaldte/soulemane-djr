liste_numbre = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

iterator = iter(liste_numbre)

# user must call next in terminal to get the next object
n = input('press enter to get the next object')

while True:
    try:
        print(next(iterator))
        n = input('press enter to get the next object')
    except StopIteration:
        break