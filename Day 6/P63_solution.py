######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########

def read_int():
    try:
        x = input()
        x = int(x)
    except Exception as e: 
        print('Bad Input {}.'.format(x))
        print('Try Again.')
        x = read_int()
        return x
    else:
        return x

def read_item_and_get_price(items):
    try:
        ii = input()
        price = items[ii]
    except Exception as e: 
        print('Available Items are {}.'.format(list(items.keys())))
        print('Try Again.')
        price = read_item_and_get_price(items)
    return int(price)

def main():
    vm = open('__VendingItems__.csv', 'r')
    items = dict([tuple(line.rstrip('\n').split('|'))  for line in vm])
    price=read_item_and_get_price(items)

    money=read_int()

    if money < price:
        print('Sorry, can not buy item. Not enough money')
    else:
        print('Thank you for your purchase. Enjoy')
        if money > price:
            print('Do not forget to collect your change, {} Rs.'.format(money - price))





if __name__ == "__main__":
    # Call the main function
    main()

######### USER CODE SECTION END #########