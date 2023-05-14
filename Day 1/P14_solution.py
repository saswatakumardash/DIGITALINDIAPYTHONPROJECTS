# Solution for P14

def main():
    # Taking an integer input s, denoting the number of seconds elapsed for a certain event.
    s = int(input())

    # Converting seconds into hours and minutes
    h = s // 3600 # Dividing by 3600 as 1 hour consists of 3600 seconds
    s = s%3600 # After conversion to hours, we need to calculate the remaining seconds as they will be converted to minutes
    m = s // 60 # Dividing by 60 as 1 minute consists of 60 seconds
    s = s % 60 # Again, after conversion to minutes, we need to calculate the remaining seconds

    print("{}:{}:{}".format(h,m,s))

# calling the main function
if __name__ == "__main__":
    main()