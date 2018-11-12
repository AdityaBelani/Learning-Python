def main():
    marks=110
    try:
        if marks<0 or marks>100:
            raise ValueError('Marks out of scope')
    finally: #This block will be executed in both the cases if try block is True or False.
        print('Bye')
    print('Prog continues after handling exception.')
if __name__ == '__main__':
    main()
