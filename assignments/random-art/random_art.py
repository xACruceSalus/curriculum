import random
from math import sin, cos, pi

# Your job is to create better version of create_expression and 
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.

def create_expression():
    """This function takes no arguments and returns an expression that 
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    expr = lambda x, y: (random.random() * 2) - 1
    return expr

def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and 
    an x and y value. It runs the expression, passing the x and y values 
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)