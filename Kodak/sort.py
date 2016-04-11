import numpy
import matplotlib.pyplot
import random


def q_sort(alist):
   q_sort_split(alist,0,len(alist)-1)

def q_sort_split(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       q_sort_split(alist,first,splitpoint-1)
       q_sort_split(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   left = first+1
   right = last

   done = False
   while not done:

       while left <= right and alist[left] <= pivotvalue:
           left = left + 1
           barGraph(alist, left, right)

       while alist[right] >= pivotvalue and right >= left:
           right = right -1
           barGraph(alist, left, right)

       if right < left:
           done = True
       else:
           temp = alist[left]
           alist[left] = alist[right]
           alist[right] = temp

   temp = alist[first]
   alist[first] = alist[right]
   alist[right] = temp
   return right



def barGraph(num_list, posi, posj):
    N = len(num_list)
    ind = numpy.arange(N)
    width = 0.5
    matplotlib.pyplot.bar(ind, num_list, width, color='green')
    matplotlib.pyplot.pause(0.2)
    matplotlib.pyplot.show()
    matplotlib.pyplot.gcf().clear()

if __name__ == '__main__':
    print "\nEnter the number of the items in list:"
    n=int(raw_input())
    num_list = []
    for i in range(0,n):
        x=random.randint(-30,50)
        num_list.append(x)
    print num_list
    matplotlib.pyplot.ion()
    q_sort(num_list)
