# Solution for P13

def main():
    #Taking the inputs for u, a and t and converting them to type float (so as to take real valued inputs).

    u = float(input())
    a = float(input())
    t = float(input())

    # Calculating the displacement using the formula d = ut + (1/2)at^2

    d = u*t + 0.5*a*t*t

    # Rounding the value to two decimal places
    d = round(d,2)

    # Finally printing the output
    print("The displacement is {}.".format(d))

# calling the main function
if __name__ == "__main__":
    main()