from algorithms import bubbleSort, selectionSort
from algorithms import mergeSort
from algorithms import insertionSort
from algorithms import quick_sort

algorithmsDict = {
    'bubble': bubbleSort,
    'merge': mergeSort,
    'insertion': insertionSort,
    'selection': selectionSort,
    'quick': quick_sort,
}


def runAlgorithm(algorithm, array):
    return algorithmsDict[algorithm](array, 0, len(array) - 1)
