######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########



def main():
    #######################################
    # Do Not Change
    roll=input()
    fileA=roll + 'A.txt'
    fileB=roll + 'B.txt'
    ########################################


    ########################################
    # Your code goes here
    inA = eval(input())
    inB = eval(input())

    with open(fileA, 'w') as A:
        for a in inA:
            A.write(str(a))
            A.write('\n')

    with open(fileB, 'w') as B:
        for b in inB:
            B.write(str(b))
            B.write('\n')
    ########################################


    ########################################
    # Do Not Change
    A, B = open(fileA, 'r'), open(fileB, 'r')
    print (A.read())
    print (B.read())
    A.close()
    B.close()
    ########################################


if __name__ == "__main__":
    # Call the main function
    main()

######### USER CODE SECTION END #########