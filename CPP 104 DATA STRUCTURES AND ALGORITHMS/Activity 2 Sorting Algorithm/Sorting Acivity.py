array1 = [3,1,2]
array2 = [5,3,8,1,2]
array3 = [10,9,8,7,6,5,4,3,2,1]
array4 = [15,1,10,12,5,8,3,9,7,6,2,11,14,13,4]
array5 = [20,18,15,16,14,13,12,10,9,7,8,6,5,4,3,2,1,11,19,17]

def bubbleSort(array):
    lenghtArray = len(array)
    for i in range(0, lenghtArray):
        for j in range(i + 1, len(array)):
            if array[i] >= array[j]:
                array[i], array[j] = array[j], array[i]

def selectionSort(array):
    lenghtArray = len(array)
    for i in range(lenghtArray):
        minElement = i
        for j in range(i + 1, lenghtArray):
            if array[j] < array[minElement]:
                minElement = j
        array[i], array[minElement] = array[minElement], array[i]

def insertionSort(array):
    lenghtArray = len(array)
    for i in range(1, lenghtArray):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def mergeSort(array):
    lenghtArray = len(array)
    if lenghtArray > 3:
        mid = lenghtArray // 2
        


#selectionSort(array3)
#insertionSort(array3)
mergeSort(array3)
print(array3)