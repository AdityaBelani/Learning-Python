import sys
def main():
    price=input('Enter the price of item:' )
    weight=input('Enter the weight of item: ')
    try:
        if price=='':price=None
        price=float(price)
        if weight=='':weight=None
        weight=float(weight)
        assert price>=0 and weight>=0 #assert: It is a validation statement. If the given condition is not satisfied an assertion error will be shown.
        result=price/weight
    except(ValueError, ZeroDivisionError):
        print('Invalid Input by User\n'+str(sys.exc_info()))
    else:
        print('Result= ',result)
if __name__ == '__main__':
    main()
