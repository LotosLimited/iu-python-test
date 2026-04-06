# my_functions.py

def math_addition(number_1, number_2):
    '''
    Mathematische Addition
    number_1: Erste Zahl
    number_2: Zweite Zahl
    return: Addition der beiden Zahlen
    '''
    result = number_1 + number_2
    return result

def math_division(number_1, number_2):
    '''
    Mathematische Division
    number_1: Erste Zahl
    number_2: Zweite Zahl
    return: Division der beiden Zahlen
    '''
    if number_2 == 0:
        raise ValueError("Du kannst nicht durch 0 teilen!")
    result = number_1 / number_2
    return result