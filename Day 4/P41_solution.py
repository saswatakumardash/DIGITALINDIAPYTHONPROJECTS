# Python program to check leap year or not
def is_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Driver Code
def main():
    # take input
    year = int(input())
    if (is_leap_year(year)):
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    main()
