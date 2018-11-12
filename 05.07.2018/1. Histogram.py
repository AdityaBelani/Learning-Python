import matplotlib.pyplot as plt
def plotHistogram(data):
    plt.hist(data)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.xlim(min(data)-1,max(data)+1)
    plt.show()
def main():
    data=input('Enter the data to be plotted as Histogram: ')
    plotHistogram(data)
if __name__ == '__main__':
    main()
