# import necessary module 
import math

def solve(n):
    if n < 10:
        return n
    s = 0
    l = math.floor(math.log(n, 10) + 1)
    while l > 0:
        s += n % 10
        n //= 10
        l -= 1
    return solve(s)

def main():
    #take input
    inp=int(input())
    print(solve(inp))

if __name__ == "__main__":
    main()