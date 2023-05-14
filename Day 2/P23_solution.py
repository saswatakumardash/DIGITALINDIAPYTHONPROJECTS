# Solution for P23

def main():
    # Taking the string input
    name = input()

    # Checking for palindrome
    cname = name.lower() # Lower casing all the characters in the string so as to avoid any case mismatching of same characters.

    rname = cname[::-1] # This operation return the reversed string.

    # Printing the output
    print(name, rname == cname) # rname == cname check if the two strings are equal or not. If they are, then True is returned, otherwise False

# calling the main function
if __name__ == "__main__":
    main()