######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import numpy as np
from scipy import linalg
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########

def main():
    # Take the input
    # eval converts the input to python lists
    a = eval(input())
    b = eval(input())

    # convert the python lists to numpy arrays
    A = np.array(a)
    B = np.array(b)

    try:
        # solve would throw an exception if its unable to find a solution
        x = linalg.solve(A, B)
    except:
        print('ERROR: Cannot find solution.')
    else:
        print(x)


if __name__ == "__main__":
    # Call the main function
    main()

######### USER CODE SECTION END #########
