# solution for P36

def main():
    myinput = input()

    vs = myinput.split(',')
    li = []

    for v in vs:
        li.append(2 * int(v))

    print(li)

if __name__ == "__main__":
    main()
