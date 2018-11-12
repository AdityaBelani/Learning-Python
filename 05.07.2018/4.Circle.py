import matplotlib.pyplot as plt
import matplotlib.patches as patches
def plotCircle(radius):
    circle=patches.Circle((0,0),radius,facecolor='green',edgecolor='red',linewidth='2.5')
    plt.gca().add_patch(circle)
    
    plt.axis('sealed')
    plt.title('circle')
    plt.show()

def main():
    radius=float(input("enter radius"))
    plotCircle(radius)

main()
                 
