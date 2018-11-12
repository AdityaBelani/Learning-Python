import matplotlib.pyplot as plt
import math
def sineCurve():
    plt.subplot(2,1,1)
    degrees=range(0,360+1)
    sineValues=[math.sin(math.radians(i)) for i in degrees]
    plt.plot(sineValues)
    plt.xlabel('Degree')
    plt.ylabel('Sine Values')
    plt.title('Sine Curve')
def main():
    sineCurve()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
