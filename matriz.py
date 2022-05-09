import random
import doctest as dt


def generateMatrix():
    list = []
    for i in range(5):
        list.append([])
        for j in range(5):
            list[i].append(random.randint(1, 10))
    return list


def findSequence(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == matrix[i][j]:
                if i < len(matrix) - 3:
                    if matrix[i + 1][j] == matrix[i][j] + 1 and matrix[i + 2][j] == matrix[i][j] + 2 and matrix[i + 3][j] == matrix[i][j] + 3:
                        return print('Sequence starts at: {}, {} and ends at: {}, {}'.format(i, j, i + 3, j))
                if j < len(matrix[i]) - 3:
                    if matrix[i][j + 1] == matrix[i][j] + 1 and matrix[i][j + 2] == matrix[i][j] + 2 and matrix[i][j + 3] == matrix[i][j] + 3:
                        return print('Sequence starts at: {}, {} and ends at: {}, {}'.format(i, j, i, j + 3))
    return print('No sequence found')


# create a test case for the function findSequence with generated matrix and check if the output is correct or not using doctest
def test_findSequence():
    """
    >>> findSequence([[1, 2, 3, 4, 6], [2, 4, 5, 7, 6], [3, 2, 1, 7, 10], [4, 6, 3, 2, 9], [9, 4, 7, 7, 4]])
    Sequence starts at: 0, 0 and ends at: 3, 0
    """
    dt.run_docstring_examples(test_findSequence, globals(), True)


if __name__ == '__main__':
    test_findSequence()
