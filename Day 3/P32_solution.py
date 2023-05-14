#solution for P32

def main():
    # take the string as input from the user
    inp = input()

    ni = inp.find('not')
    bi = inp.find('bad')
    if ni == -1:
        # 'not' not found.
        print(inp)
    elif bi == -1:
        # 'bad' not found
        print(inp)
    elif ni > bi:
        # 'not' after 'bad'
        print(inp)
    else:
        # all conditions satisfied.
        bi = bi + len('bad')
        op = inp[:ni] + 'good' + inp[bi:]
        print(op)

if __name__ == "__main__":
    main()
