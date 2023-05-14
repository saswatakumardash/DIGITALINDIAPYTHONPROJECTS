# Template for P24

def main():
    # Taking the input
    inp = input()

    # We first find the position of 'not' in our input string.
    s = inp.find('not') # This returns the index of 'n' in the occurrence of the word 'not'

    # We then find the position of 'bad' in our input string.
    e = inp.find('bad') # This returns the index of 'b' in the occurrence of the word 'bad'

    r = inp[:s] + 'good' + inp[e+3:] # We then take the part of string before 'not' and the part of string after 'bad' and append 'good' in between them.

    # Printing the modified string.
    print(r)

# calling the main function
if __name__ == "__main__":
    main()