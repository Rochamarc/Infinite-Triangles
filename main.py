from classes import Line
from functions import generate_images
from math_functions import generate_points
from random import choice 

value_range = int(input("Type the max range of the points [min 10]>. ")) # Define the range of the points between 0 and n
points_insert = int(input("Type the numbers of points you wanna insert [min 5]>. ")) # Define the range of points to be insert between 0 and n


# Generate and set the original points
A, B, C = generate_points(value_range)
points = [ A, B, C ]
xs, ys = [ i[0] for i in points ], [ i[-1] for i in points ]

generate_images(xs, ys)

lines = [ Line(A,B), Line(B,C), Line(A,C)]

for _ in range(points_insert):
    pointer = choice(lines) # choose a line between two points to insert a new point
    middle_point = pointer.middle_point() # defines a middle point

    # inserting the point into the points
    xs.append(middle_point[0])
    ys.append(middle_point[-1])

    # update with new lines and new point
    lines += [ Line(middle_point, point) for point in points ]
    points.append(middle_point)

    # show to final user
    generate_images(xs, ys)