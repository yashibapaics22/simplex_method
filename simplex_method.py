print("THIS IS THE PROGRAM TO FIND THE INTERSECTING POINT OF LINEAR EQUATIONS")
print()
print("""Format of Equation should be :- 'Ax + By + C = 0' """)
print()
print("This program is valid for only 2 variable linear Equations")

n = int(input("Enter the number of equations you have : "))
print()
if(n == 2):
    # INPUT OF EQUATION 1:
    a1 = int(input("Enter the coefficient of x in Equation1 : "))
    b1 = int(input("Enter the coefficient of y in Equation1 : "))
    c1 = int(input("Enter the constant of Equation 1 : "))

    print()

    # INPUT OF EQATION 2:
    a2 = int(input("Enter the coefficient of x in Equation2 : "))
    b2 = int(input("Enter the coefficient of y in Equation2 : "))
    c2 = int(input("Enter the constant of Equation2 : "))

    print()

    # CALCULATION:

    y = (a2*c1-a1*c2)/(a1*b2-a2*b1)
    x = -((c1+b1*y)/a1)
    fx = "{:.2f}".format(x)
    fy = "{:.2f}".format(y)

    # PRINTING:
    print(fx,",",fy)
    
if(n==3) :
    # INPUT OF EQUATION 1:
    a1 = int(input("Enter the coefficient of x in Equation1 : "))
    b1 = int(input("Enter the coefficient of y in Equation1 : "))
    c1 = int(input("Enter the constant of Equation 1 : "))

    print()

    # INPUT OF EQATION 2:
    a2 = int(input("Enter the coefficient of x in Equation2 : "))
    b2 = int(input("Enter the coefficient of y in Equation2 : "))
    c2 = int(input("Enter the constant of Equation2 : "))

    print()

    # INPUT OF EQUATION 3:
    a3 = int(input("Enter the coefficient of x in Equation3 : "))
    b3 = int(input("Enter the coefficient of y in Equation3 : "))
    c3 = int(input("Enter the constant of Equation3 : "))

    print()

    # CALCULATION:

    det = a1*(b2*c3 - c2*b3) - a2*(b1*c3 - b3*c1) + a3*(b1*c2 - c1*b2)


    # PRINTING:

    print(det)
    if(det == 0):   
        ey = (a2*c1-a1*c2)/(a1*b2-a2*b1)
        ex = -((c1+b1*ey)/a1)
        fex = "{:.2f}".format(ex)
        fey = "{:.2f}".format(ey)
        print("These lines are intersect each other at a point")
        print("The point of intersection is : ", fex,",",fey ) 

    else:
        print("These lines are not intersect each other at a particular point")
else:
    print("SORRY!,  Program is not valid for given input")
