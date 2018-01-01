"""Define a custom exception class which takes a string message as attribute."""


class OwnException(Exception):

    def __init__(self, message):
        self.message = message
   # def __call__(self,):
    #    print("You are trying to call class instance")

error = OwnException("Error")