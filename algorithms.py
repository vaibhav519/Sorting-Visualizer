from display import handleDrawing


def bubbleSort(array, *args):
    size = len(array)
    for i in range(size):
        for j in range(size - i - 1):
            handleDrawing(array, j, j + 1, -1, -1)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def mergeSort(array, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(array, left, mid)
        mergeSort(array, mid + 1, right)
        merge(array, left, mid, right)


def merge(array, left, mid, right):
    L = array[left:mid + 1]
    R = array[mid + 1:right + 1]
    i = 0
    j = 0
    k = left
    while i < len(L) and j < len(R):
        handleDrawing(array, left + i, mid + j, left, right)
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        array[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        array[k] = R[j]
        j += 1
        k += 1


mySortedRows = []


def insertionSort(array, *args):
    size = len(array)
    for i in range(0, size):
        j = i - 1
        key = array[i]
        mySortedRows.append(i)
        while j >= 0 and array[j] > key:
            handleDrawing(array, j, -1, i, -1, greenRows=mySortedRows)
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    mySortedRows.clear()


def selectionSort(array, *args):
    for i in range(0, len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            handleDrawing(array, j, -1, i, -1, greenRows=mySortedRows)
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


def partition(array, start, end):
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:

        while start < len(array) and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if start < end:
            array[start], array[end] = array[end], array[start]

        handleDrawing(array, end, end, start, -1)

    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end


def quick_sort(array, start, end):
    if start < end:
        p = partition(array, start, end)
        quick_sort(array, start, p - 1)
        quick_sort(array, p + 1, end)
