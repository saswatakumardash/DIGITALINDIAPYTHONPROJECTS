# solution for P34

def main():
    # take input
    N = int(input())

    for i in range(N):
        for j in range(i+1):
            print('*',end='')
        print()

if __name__ == "__main__":
    main()
