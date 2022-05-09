import random


def randomNumber():
    return random.randint(1, 100)


def genList():
    list = [{'id': 1, 'age': randomNumber()}, {'id': 2, 'age': randomNumber()}, {
        'id': 3, 'age': randomNumber()}, {'id': 4, 'age': randomNumber()}, {'id': 5, 'age': randomNumber()}, {'id': 6, 'age': randomNumber()}, {'id': 7, 'age': randomNumber()}, {'id': 8, 'age': randomNumber()}, {'id': 9, 'age': randomNumber()}, {'id': 10, 'age': randomNumber()}]
    return list


def sortListHighToLow(list):
    list.sort(key=lambda x: x['age'], reverse=True)
    return list


list = genList()


print(sortListHighToLow(list))
