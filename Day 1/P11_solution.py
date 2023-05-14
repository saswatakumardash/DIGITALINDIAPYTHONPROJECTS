# Solution for P11

def main():
    # Taking input for temperature in Fahrenheit.
    F = float(input())

    # Calculating the temperature in Celsius (C) using the formula C=(F−32)×5/9.
    C = float( (F-32)*float(5/9) )

    # Also, round the value obtained to two decimal places.
    C = round(C,2)

    # Print the answer
    print("Fahrenheit temperature {:.2f} is the same as {:.2f} degrees Celsius.".format(F,C))

# calling the main function
if __name__ == "__main__":
    main()