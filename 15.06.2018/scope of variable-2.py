a=4
def f():
    a=5
    def g():
        nonlocal a
        a=10
        print ('Inside fn g(), a= ',a)
        def h():
            nonlocal a
            a=20
            print ('Inside fn h(), a= ',a)
        h()
    g()
    print ('Inside fn f(), a= ',a)
f()
