import numpy
import matplotlib.pyplot

'''
This code illustrates a bargraph representation of the the insertion sort in 
each iteration. 
>>>We have used 3 different colored bars in the graph.
>>>The green and red bars reperesent the 2 numbers currently being compared. 
>>>The blue bars represent the numbers which are represent the other numbers.
'''


def insertionsort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        bar(alist, index - 1, index, index)
        while position > 0 and alist[position-1] > currentvalue:
            bar(alist, position-1, position, index)
            alist[position] = alist[position-1]
            bar(alist, position-1, position, index)
            position = position-1
            alist[position] = currentvalue
        if position != index: 
            bar(alist, position, position+1, index)	
    return alist


def bar(alist, r, g, label):
    N = len(alist)
    ind = numpy.arange(N)
    width = 0.25
    barlist = matplotlib.pyplot.bar(ind, alist, width, color='b')
    barlist[r].set_color('r')
    barlist[g].set_color('g')
    matplotlib.pyplot.xlabel("Iteration number: %d" % (label))
    matplotlib.pyplot.pause(2)
    matplotlib.pyplot.show()
    matplotlib.pyplot.gcf().clear()

if __name__ == '__main__':
    alist = [
        3, 1, 2, 5, 4
        ]
    print alist
    matplotlib.pyplot.ion()
    insertionsort(alist)

    