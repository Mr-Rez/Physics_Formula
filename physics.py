# Physics Formula Solver

# Note: This is incomplete and I will finish it later 



which_formula = int(input("Which formula you want me to solve >> \n 1.Motion \n 2.Force \n 3.Pressure \n 4.Density \n 5.Sound \n 6.Waves \n >> "))

if which_formula == 1:
    all_motion_formula = int(input("Which of the following formula you need to solve: \n 1.Acceleration \n 2.Equations of Motion \n 3.Laws of Falling Bodies \n >>> "))
    if which_formula == 1:
        ask_acc = input("In Acceleration which value you wanna find out?  Time(t), Orginal_Velocity(u), Last_Velocity(v), Acceleration(a) >> ")
        if ask_acc =="a":
            v = float(input("Enter the value of 'v' > "))
            u = float(input("Enter the value of 'u' > "))
            t = float(input("Enter the value of 't' > "))
            a = (v - u ) / t
            print("Acceleration =" , a)
        if ask_acc == "v":
            ask_v = input("Do you have the value of Orginal_Velocity(u) > y/n >> ")
            if ask_v == y:
                u = float(input("Enter the value of 'u' > "))
                a = float(input("Enter the value of 'a' > "))
                t = float(input("Enter the value of 't' > "))
                v = u + a*t
                print("Velocity =" , v)
            elif ask_v == "n":
                a = float(input("Enter the value of 'a' > "))
                t = float(input("Enter the value of 't' > "))
                v = a*t
                print("Velocity =" , ve)
        if ask_acc == "u":
            v = float(input("Enter the value of 'v' > "))
            a = float(input("Enter the value of 'a' > "))
            t = float(input("Enter the value of 't' > "))
            u = (v - a) / t
            print("Last_Velocity =" , u)
        if ask_acc == "t":
            a = float(input("Enter the value of 'a' > "))
            v = float(input("Enter the value of 'v' > "))
            u = float(input("Enter the value of 'u' > "))
            t = (v - u) / a
            print("Time =" , t)
    elif which_formula == 2:
        u = float(input("Enter the value of 'u' >> "))
        t = float(input("Enter the value of 't' >> "))
        a = float(input("Enter the value of 'a' >> "))
        s = (u * t) + 0.5*a*t**2
        print("S = ", s )
    elif which_formula == 3:
        u = float(input("Enter the value of 'u' >> "))
        g = 9.8
        t = float("Enter the value of 't' >> ")
        v = u + g*t
        print("V = ", v)