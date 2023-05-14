# solution for P45

# definition TowerOfHanoi function
def hanoi_c(n, A, C, B):
  if n==0:
    return 0 # nothing to move!!
    # recursively move n-1 disks 
    # from A to B using C as auxx
  count = hanoi_c(n-1, A, B, C)
    # atomic move of a single disk
  count += 1
    # recursively move n-1 disks 
    # from B to C using A as auxx
  count += hanoi_c(n-1, B, C, A)
  return count

 
def main():
  #take input as number of disks
  disks = int(input())
  #call TowerOfHanoi function 
  count=hanoi_c(disks, 'A', 'B', 'C')
  print("Number of moves:",count)


if __name__ == "__main__":
    main()

# Simplfied way is to solve the Recurrence:
# Moves(n) = Moves(n-1) + 1 + Moves(n-1)
#          = 2*Moves(n-1) + 1
# Solution to the recurrence is 2**n - 1.