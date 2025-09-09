#Lec1 wk1
# An example of Refactoring - using a common function.

def get_positive_value(message):
    value = float(input(message))
    while value <= 0.0:
        value = float(input("The value must be greater than zero\n" + message))
    return value

while True:
    r1 = get_positive_value("What is resistance 1 in ohms? ")
    r2 = get_positive_value("What is resistance 2 in ohms? ")