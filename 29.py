"""Question: 29
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print al l strings line by line."""


def strlen(arg1, arg2):

    if len(arg1) > len(arg2):
        print(arg1)

    elif len(arg2) > len(arg1):
        print(arg2)

    else:
        print("{0}\n{1} ".format(arg1, arg2))


