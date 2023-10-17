'''
QUESTION:
Write a python program to calculate the area of geometric shapes

ALGORITHM:
1) Start
2) Get the input from the user of which shape they want to find the area.
3) According to the given shape, get the varibles which are required for the calculation of area. 
4) Calculate the area and store it. Print the area calculated. 
5) If the input is not in the menu then, print that the input is invalid.
6) Stop
'''

while True:
    print("\n" + "MENU".center(20))
    print("1) Triangle\n2) Square/Rectangle\n3) Parallelogram/Rhombus\n4) Trapezium\n5) Circle\n6) Ellipse")
    n = int(input("Enter your choice: "))

    if n == 1:
        base = float(input("Enter base of the triangle: "))
        height = float(input("Enter height of the triangle: "))
        triangle_area = 0.5 * base * height
        print("\nThe area of the triangle of base", base, "and height", height, "is", triangle_area)

    elif n == 2:
        side1 = float(input("Enter the length of side1: "))
        side2 = float(input("Enter the length of side2: "))
        quad1_area = side1 * side2
        print("\nThe area of the quadrilateral of side lengths", side1, "and", side2, "is", quad1_area)

    elif n == 3:
        qbase = float(input("Enter the base of parallelogram/rhombus: "))
        qheight = float(input("Enter the height of the parallelogram/rhombus: "))
        quad2_area = qbase * qheight
        print("\nThe area of the quadrilateral of base", qbase, "and height", qheight, "is", quad2_area)

    elif n == 4:
        sidea = float(input("Enter side a: "))
        sideb = float(input("Enter side b: "))
        theight = float(input("Enter height: "))
        trap_area = ((sidea + sideb) / 2) * theight
        print("\nThe area of the trapezium with side a", sidea, ", side b", sideb, "and height", theight, "is", trap_area)

    elif n == 5:
        radius = float(input("Enter the radius: "))
        circ_area = 3.14 * radius * radius
        print("\nThe area of the circle of radius", radius, "is", circ_area)

    elif n == 6:
        major = float(input("Enter the major axis: "))
        minor = float(input("Enter the minor axis: "))
        ellipse_area = 3.14 * major * minor
        print("\nThe area of the ellipse of major axis", major, "and minor axis", minor, "is", ellipse_area)

    else:
        print("\nError")

    yn = input("Do you want to continue? (y/n)")
    if yn.lower() == 'n':
        break
