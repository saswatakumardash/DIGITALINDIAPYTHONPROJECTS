4
# solution for P35

def main():
    # take input
    N = int(input())
    LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(N):
        print('_',end='')
        for j in range(i+1):
            print(LETTERS[j], end='_')
        print()

if __name__ == "__main__":
    main()
