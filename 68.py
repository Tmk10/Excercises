"""Please write a binary search function which searches an item in a sorted list.
The function should return the index of element to be searched in the list.


Hints:
Use if/elif to deal with conditions."""

import math


def search(list, value):
    index = -1
    bottom = 0
    top = len(list)

    while index == - 1 and top > bottom:
        mid = int(math.floor((top + bottom) / 2))
        if value == list[mid]:
            index = mid
        elif value < list[mid]:
            top = mid - 1
        else:
            bottom = mid + 1

    return index



lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(search(lista, 1))


