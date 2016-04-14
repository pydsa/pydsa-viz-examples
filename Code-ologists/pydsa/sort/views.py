from django.shortcuts import render, Http404
from django.http import HttpResponse, JsonResponse
from sort.models import Sorting
from django.template import RequestContext, loader
import numpy
import matplotlib.pyplot
import json


# Create your views here.
big_list = [""]


def detail(request, sorting_no):
    try:
        sorting_ob = Sorting.objects.order_by('Name')[0]
    except Sorting.DoesNotExist:
        raise Http404("Error")

    return render(request, 'sort/detail.html', {'sorting_ob': sorting_ob})


def index(request):
    # Create dummy objects to show example of Bubble sort
    sort_obj = Sorting.objects.get_or_create(Name="Bubble Sort",
                                             List="25,216,180,150,126,103,44")
    sort_algo = Sorting.objects.order_by('Name')[0:5]
    context = {'sort_algo': sort_algo}
    return render(request, 'sort/index.html', context)


def bubbleSort(num_list):
    '''
    This fun() will sort the list provided as argument.
    And after each iteration barGraph() will be involked
    '''
    for posi in xrange(0, len(num_list) - 1, 1):
        for posj in xrange(0, len(num_list) - 1, 1):
            big_list.append(num_list[:])
            if num_list[posj] > num_list[posj+1]:
                num_list[posj], num_list[posj+1] = (num_list[posj+1],
                                                    num_list[posj])

    return num_list


def json_func(request):
    big_list[:] = []
    try:
        sorting_ob = Sorting.objects.order_by('Name')[0]
    except Sorting.DoesNotExist:
        raise Http404("Error")
    my_list = sorting_ob.List.split(",")
    my_list = [int(x) for x in my_list]
    my_list = bubbleSort(my_list)
    if request.method == 'GET':
        return JsonResponse(big_list, safe=False)
