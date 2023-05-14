# Solution for P22

def main():
    # Taking the inputs
    text = input()
    key = input()

    # Using the inbuilt count function of string to count the number of occurrences of key in the input text.
    count = text.count(key)

    # Printing the count
    print(count)

# calling the main function
if __name__ == "__main__":
    main()