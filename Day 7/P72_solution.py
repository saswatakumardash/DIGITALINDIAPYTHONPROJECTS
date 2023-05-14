######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########

def main():
    # Take the input
    v = float(input())
    a = math.radians(float(input()))  # Need to convert the angle into radians
    g = 9.8  # defines the gravitational force

    # calculate the velocities in x and y direction, as well as time and distance
    vy = v * math.sin(a)  # velocity of object in y direction (v * sin(a))
    y = vy * vy / (2 * g)  # peak horizontal distance covered by the object

    t = 2 * 2 * y / vy  # time of flight

    vx = v * math.cos(a)  # velocity of object in x direction (v * cos(a))
    d = vx * t  # total distance covered

    # To plot the trajectory of the object we have to calculate its position (in X and Y directions) at various times
    T = np.arange(0, t, 0.01)  # Generates a numpy array having values from 0 to 't' with an interval size of 0.01
    Y = vy * T - 0.5 * g * T * T  # Calculate the objects Y position at various times
    X = vx * T  # Calculate the objects X position at various times

    # Plot the trajectory
    plt.plot(X, Y)
    plt.xlabel('Horizontal Distance (m)')
    plt.ylabel('Vertical Height (m)')
    plt.show()

    # Output the calculated values
    print('Time of Flight = {}'.format(round(t, 2)))
    print('Distance Covered = {}'.format(round(d, 2)))
    print('Peak Height = {}'.format(round(y, 2)))


if __name__ == "__main__":
    # Call the main function
    main()
########## USER CODE SECTION END #########
