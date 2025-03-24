import random 

def generate_points(value_range: int) -> list[list]:
    """Generate three diferent cartesian coordinates (A, B and C belonging to R²) based on the range

    Parameters
    ----------
    value_range : int
        Value that defines the range of the x and y coordinates

    Returns 
    -------
    list[list] : [ [x1, y1], [x2, y2], [x3, y3] ]
    """
    
    # defines the values
    values = [ i for i in range(value_range) ]
    x,y = values.copy(), values.copy()

    random.shuffle(x)
    random.shuffle(y)

    return [[x.pop(), y.pop()], [x.pop(), y.pop()], [x.pop(), y.pop()]]

if __name__ == "__main__":

    # A, B, C = generate_points(20)

    # print(A, B, C)

    # a = [6,1]
    # b = [3,5]

    # l = Line(a, b)
    # l.equation_line()
    # c = l.middle_point()

    # print(c)
    ...
