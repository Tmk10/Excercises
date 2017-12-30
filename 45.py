"""Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]."""

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x: x ** 2, list(filter(lambda x: x % 2 == 0, data))))

print(result)
