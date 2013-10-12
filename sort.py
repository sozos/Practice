#!/usr/bin/python
import random
import copy

#=======#
# SORTS #
#=======#
#def selectionSort(A)
#def insertionSort(A)
#def quickSort(A, left, right)
#def shellSort(A)
#def mergeSort(A, left, right)
#def countingSort(A)
#def radixSort(A)
#def bucketSort(A)

#=========#
# HELPERS #
#=========#
#def createRandomIntArray(size, minVal, maxVal)
#def generateIntArray(size)
#def isSorted(input)
#def choosePivot(A, left, right)
#def partition(A, left, right)
#def merge(A, Lstart, Lend, Rstart, Rend)
#def convertStringToInt(A)

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

def merge(A, Lstart, Lend, Rstart, Rend):
    merged = []
    l = Lstart
    r = Rstart

    while True:
        # If one of the sublists is exhausted, just append the rest of the other sublist
        if (l > Lend):
            merged += A[r:Rend+1]
            break;

        if (r > Rend):
            merged += A[l:Lend+1]
            break;

        # Add the smaller value to the merged array, then advance pointer
        if (A[l] < A[r]):
            merged.append(A[l])
            l += 1
        else:
            merged.append(A[r])
            r += 1

    # Sanity check
    if (len(merged) != (Lend - Lstart + 1) + (Rend - Rstart + 1)):
        print "ERROR IN MERGING"

    # Reflect updated merged section into actual array
    for i in range(Lstart, Rend+1):
        A[i] = merged[i - Lstart]

def mergeSort(A, left, right):
    if (left == right):
        return A
    else:
        mid = (left+right)/2 # Python division truncates remainders
        mergeSort(A, left, mid)
        mergeSort(A, mid+1, right)
        merge(A, left, mid, mid+1, right)
        return A

def countingSort(A):
    # Obtain min/max values of input
    minVal = A[0]
    maxVal = A[0]
    for i in range(0, len(A)):
        if A[i] < minVal:
            minVal = A[i]
        if A[i] > maxVal:
            maxVal = A[i]

    # Create counter and output arrays
    counter = []
    for i in range(minVal, maxVal+1):
        counter.append(0)

    # Count occurences + Create output array
    output = []
    for i in range(0, len(A)):
        counter[A[i]-minVal] += 1
        output.append(0)

    # Cumulate counts
    for i in range(1, len(counter)):
        counter[i] += counter[i-1]

    # Sanity check
    if counter[len(counter)-1] != len(A):
        print "ERROR IN COUNTING"

    for i in range(0, len(A)):
        output[counter[A[i]-minVal]-1] = A[i]
        counter[A[i]-minVal] -= 1

    return output

def convertStringToInt(A):
    converted = []
    for i in range(0, len(A)):
        converted.append(int(A[i]))
    return converted

def radixSort(A):
    base = 10 # Assume base = 10. In general, this might not always be the case
    converted = []
    maxLength = 0
    # Count max length
    for i in range(0, len(A)):
        converted.append(str(A[i]))
        maxLength = max(maxLength, len(converted[i]))

    # Pad zeroes in front till same length
    for i in range(0, len(converted)):
        while len(converted[i]) < maxLength:
            converted[i] = "0" + converted[i]

    A = converted

    # Sort from 'least significant bit' to 'most significant bit'
    for l in reversed(range(0, maxLength)):
        sublists = []
        for b in range(0, base):
            sublists.append([])

        # Add each item to its appropriate sublist
        for i in range(0, len(converted)):
            sublists[int(A[i][l])].append(A[i])

        # Sort the sublists based on the length index [Modified Insertion sort]
        for b in range(0, base):
            for i in range(0, len(sublists[b])):
                for j in reversed(range(1, i+1)):
                    if (sublists[b][j][l] < sublists[b][j-1][l]):
                        temp = sublists[b][j]
                        sublists[b][j] = sublists[b][j-1]
                        sublists[b][j-1] = temp

        # Concatenate lists
        A = []
        for b in range(0, base):
            A += sublists[b]

    return convertStringToInt(A)

def bucketSort(A):
    # Obtain min/max values of input
    minVal = A[0]
    maxVal = A[0]
    for i in range(0, len(A)):
        if A[i] < minVal:
            minVal = A[i]
        if A[i] > maxVal:
            maxVal = A[i]

    # Create n buckets
    buckets = []
    for i in range(0, len(A)):
        buckets.append([])

    # Put items into buckets
    for i in range(0, len(A)):
        index = (A[i]-minVal)/(maxVal-minVal)
        buckets[index].append(A[i])

    # Sort each bucket [Insertion sort]
    for b in range(0, len(buckets)):
        for i in range(0, len(buckets[b])):
            for j in reversed(range(1, i+1)):
                if (buckets[b][j] < buckets[b][j-1]):
                    temp = buckets[b][j]
                    buckets[b][j] = buckets[b][j-1]
                    buckets[b][j-1] = temp

    # Concatenate buckets
    A = []
    for b in range(0, len(buckets)):
        A += buckets[b]

    return A

#======#
# MAIN #
#======#

n = input()
A = createRandomIntArray(n, 0, n)
#A = generateIntArray(n) # Distinct sequence of integers
print "Input: ", A

B = selectionSort(copy.deepcopy(A))
C = insertionSort(copy.deepcopy(A))
#D = quickSort(copy.deepcopy(A), 0, len(A)-1)
E = shellSort(copy.deepcopy(A))
F = mergeSort(copy.deepcopy(A), 0, len(A)-1)
G = countingSort(copy.deepcopy(A))
H = radixSort(copy.deepcopy(A))
I = bucketSort(copy.deepcopy(A))

print "Selection Sort: ", B, isSorted(B)
print "Insertion Sort: ", C, isSorted(C)
#print "Quick Sort: ", D, isSorted(D)
print "Shell Sort: ", E, isSorted(E)
print "Merge Sort: ", F, isSorted(F)
print "Counting Sort: ", G, isSorted(G)
print "Radix Sort: ", H, isSorted(H)
print "Bucket Sort: ", I, isSorted(I)
