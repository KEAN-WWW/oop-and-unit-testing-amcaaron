class Calculator(object):
    @staticmethod
    def addition(self, val1, val2):
        return add(val1, val2)

    @staticmethod
    def subtraction(self, val1, val2):
        return subtract(val1, val2)

    @staticmethod
    def multiplication(self, val1, val2):
        return multiply(val1, val2)

    @staticmethod
    def division(self, val1, val2):
        return divide(val1, val2)

def add(val1:int, val2:int) -> int:
    return val1 + val2

def subtract(val1:int, val2:int) -> int:
    return val1 - val2

def multiply(val1:int, val2:int) -> int:
    return val1 * val2

def divide(val1:int, val2:int) -> int:
    return val1 // val2