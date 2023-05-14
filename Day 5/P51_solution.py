######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########


def main():
    N=int(input())
    M=int(input())

    inEdges = dict()
    for i in range(N):
        inEdges[i] = set()

    for i in range(M):
        i,j  = input().split(',')
        i = int(i)
        j = int(j)
        if i >= N or j >= N or i < 0  or j < 0:
            continue #invalid edge
        inEdges[j].add(str(i))

    k=int(input())
    if k >= N or k < 0:
        print("ERROR: Invalid Node.")
    else:
        print(",".join(sorted(inEdges[k])))


if __name__ == "__main__":
    # Call the main function
    main()

######### USER CODE SECTION END #########