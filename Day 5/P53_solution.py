######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########


def main():
	s=input()
	freq=dict()

	for c in s:
		if c in freq:
			freq[c]+=1
		else:
			freq[c]=1

	result=', '.join('{}:{}'.format(k,v) for k,v in freq.items())
	print(result)



if __name__ == "__main__":
    # Call the main function
    main()

######### USER CODE SECTION END #########