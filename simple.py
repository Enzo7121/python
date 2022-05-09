import random
import doctest as dt


def randomNumber():
    return random.randint(1, 100)


def createList():
    list = []
    for i in range(10):
        list.append({})
        list[i]['id'] = i
        list[i]['age'] = randomNumber()
    return list


def sortListHighToLow(list):
    list.sort(key=lambda x: x['age'], reverse=True)
    return list


def test_sortListHighToLow():
    """
    >>> list = [{"id": 0, "age": 10}, {"id": 1, "age": 20}, {"id": 2, "age": 30}, {"id": 3, "age": 40}, {"id": 4, "age": 50}, {"id": 5, "age": 60}, {"id": 6, "age": 70}, {"id": 7, "age": 80}, {"id": 8, "age": 90}, {"id": 9, "age": 99}]
    >>> sortListHighToLow(list)
    [{'id': 9, 'age': 99}, {'id': 8, 'age': 90}, {'id': 7, 'age': 80}, {'id': 6, 'age': 70}, {'id': 5, 'age': 60}, {'id': 4, 'age': 50}, {'id': 3, 'age': 40}, {'id': 2, 'age': 30}, {'id': 1, 'age': 20}, {'id': 0, 'age': 10}]
    """
    dt.run_docstring_examples(test_sortListHighToLow, globals(), True)


if __name__ == '__main__':
    test_sortListHighToLow()
