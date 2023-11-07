pi = 3.15159

def circumference(radius):
    return 2*pi*radius

def area(radius):
    return pi * radius**2

def arc_length(radius, angle):
    return radius * angle

def arc_area(radius, angle):
    return area(radius) * angle/(2*pi)
