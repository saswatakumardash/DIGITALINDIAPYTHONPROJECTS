# Solution for P12

def main():
    #Taking the inputs for u, a and t.

    u = float(input())
    a = float(input())
    t = float(input())

    # Calculating the final velocity using the formula v = u + at

    v = u + a*t

    # Rounding the value to two decimal places
    v = round(v,2)

    # Finally printing the output
    print("The final velocity is {}.".format(v))

# calling the main function
if __name__ == "__main__":
    main()