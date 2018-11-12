import matplotlib.pyplot as plt
x=[2,4,6,8,10]
y=[3,5,7,9,11]
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.plot(x,y,'r*--',markersize=10.5, linewidth=2.2)
plt.axis([1,11,2,12])
plt.xlabel('x')
plt.ylabel('x*x')
plt.title('Sample Program')
plt.show()
