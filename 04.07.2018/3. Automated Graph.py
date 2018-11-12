import matplotlib.pyplot as plt
def plotfunctions(a,b,step):
    nsteps=int((b-a)/step)
    x=[a+step*i for i in range(nsteps+1)]
    y1=[t**2 for t in x]
    y2=[t**3 for t in x]
    plt.plot(x,y1,'ro--',label='x vs x**x')
    plt.plot(x,y2,'b<-.',label='x vs x*x*x')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('x vs square x, and x vs cube x')
    plt.grid()
    plt.show()

def main():
    a=float(input('Enter first Element of Range: '))
    b=float(input('Enter last Element of Range: '))
    step=float(input('Enter the step size: '))
    plotfunctions(a,b,step)

if __name__ == '__main__':
    main()
