#!/bin/python
import random
import copy

#=======#
# SORTS #
#=======#
#def selectionSort(A)
#def insertionSort(A)
#def quickSort(A, left, right)
#def shellSort(A)

#=========#
# HELPERS #
#=========#
#def createRandomIntArray(size, minVal, maxVal)
#def generateIntArray(size)
#def isSorted(input)
#def choosePivot(A, left, right)
#def partition(A, left, right)

def createRandomIntArray(size, minVal, maxVal):
    Arr = []
    for i in range(size):
        Arr.append(random.randint(minVal, maxVal))
    return Arr

def generateIntArray(size):
    Arr = range(size)
    random.shuffle(Arr)
    return Arr

def isSorted(input):
    n = len(input)
    val = input[0]
    for i in range(1, n):
        if (input[i] < val):
            return False
        val = input[i]
    return True

def selectionSort(A):
    n = len(A)
    for i in reversed(range(1, n)):
        maxIndex = i
        for j in reversed(range(0, i)):
            if A[maxIndex] < A[j]:
                maxIndex = j
        temp = A[maxIndex]
        A[maxIndex] = A[i]
        A[i] = temp
    return A

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        for j in reversed(range(1,i+1)):
            if (A[j] < A[j-1]):
                temp = A[j-1]
                A[j-1] = A[j]
                A[j] = temp
    return A

def choosePivot(A, left, right):
    # Pick first element
    #return A[left]
    # Pick random element
    return A[random.randint(left, right)]

# Left half will be <= pivot
# Right half will be > pivot
def partition(A, left, right):
    pivotVal = choosePivot(A, left, right)
    i = left
    j = right

    while True:
        while (A[j] > pivotVal):
            j -= 1
        while (A[i] < pivotVal):
            i += 1
        if i < j:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
        else: # Pointers have crossed over
            return j

# Works only for distinct elements in A
def quickSort(A, left, right):
    if left < right:
        split = partition(A, left, right)
        quickSort(A, left, split)
        quickSort(A, split+1, right)
    return A

def shellSort(A):
    n = len(A)
    seq = range(1,n,3) # seq can be replaced

    for gap in reversed(seq):
        for i in range(gap, n):
            temp = A[i]
            j = i

            # Assume subarrays (w.r.t. mod gap) involving A[0]-A[j]
            # Insert A[j] into its correct position in its respective (mod gap) subarray
            # "Mini insertion sort"
            while (j >= gap):
                if (A[j-gap] > temp):
                    A[j] = A[j-gap]
                    j -= gap
                else:
                    break;
            A[j] = temp
    return A

#======#
# MAIN #
#======#

n = input()
#A = createRandomIntArray(n, 0, n)
A = generateIntArray(n)
print "Input: ", A

B = selectionSort(copy.deepcopy(A))
C = insertionSort(copy.deepcopy(A))
D = quickSort(copy.deepcopy(A), 0, len(A)-1)
E = shellSort(copy.deepcopy(A))

print "Selection Sort: ", B, isSorted(B)
print "Insertion Sort: ", C, isSorted(C)
print "Quick Sort: ", D, isSorted(D)
print "Shell Sort: ", E, isSorted(E)
