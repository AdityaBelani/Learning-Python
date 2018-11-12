import matplotlib.pyplot as plt
def plotpie(data,labels):
    plt.pie(data,labels=labels,autopct='%2f')
    plt.title('Pie Chart')
    plt.show()
    
def main():
    data=input('Enter data to be plotted: ')
    labels=input('Enter the labels: ')
    plotpie(data,labels)
    
if __name__ == '__main__':
    main()
