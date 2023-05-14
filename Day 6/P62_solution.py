######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########

def main():
    roll=input()
    fileA=roll + 'A.txt'
    fileB=roll + 'B.txt'

    item=input()

    fA = False
    fB = False

    with open(fileA, 'r') as A:
        LA = A.readlines()
    with open(fileB, 'r') as B:
        LB = B.readlines()
        
    fA = item+'\n' in LA
    fB = item+'\n' in LB

    if fA and fB:
        print("Item {} found in both {} and {}".format(item, fileA, fileB))
    elif fA:
        print("Item {} found in {}".format(item, fileA))
    elif fB:
        print("Item {} found in {}".format(item, fileB))
    else:
        print("Item {} found nowhere".format(item))




if __name__ == "__main__":
    # Call the main function
    main()

######### USER CODE SECTION END #########