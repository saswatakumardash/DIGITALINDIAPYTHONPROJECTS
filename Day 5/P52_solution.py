######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import sys, os
import string
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########



alphabet = set(string.ascii_lowercase) 
  
def ispangram(s): 
    schar = set(s.lower())
    return (schar >= alphabet, sorted(list(alphabet - schar)))
      
# Driver code 
def main():
    s = input()
    flag, missing = ispangram(s)
    if flag:
        print("Yes, the string is a pangram.") 
    else: 
        misstr = ", ".join(missing)
        print("No, the string is NOT a pangram. Missing letter(s) is(are) {}.".format(misstr))


if __name__ == "__main__":
    # Call the main function
    main()

######### USER CODE SECTION END ######### 