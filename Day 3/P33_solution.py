#solution for P33
def main():
    # take input as number
    nums = input()
    numi = int(nums)

    sum = 0
    # computing sum of cubes of the digits of the number
    for ds in nums:
        di = int(ds)
        sum += di ** 3

    same = "the"
    # comparing sum with num whether both are equal or not
    if (sum != numi):
        same = "NOT"
    print('Sum of Cubes is {}. It is {} same as the number {}.'.format(sum, same, nums))


if __name__ == "__main__":
    main()

