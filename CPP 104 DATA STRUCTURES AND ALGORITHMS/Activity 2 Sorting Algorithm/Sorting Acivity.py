
def bubbleSort(array):
    lenghtArray = len(array)
    for i in range(0, lenghtArray):
        for j in range(i + 1, lenghtArray):
            if array[i] >= array[j]:
                array[i], array[j] = array[j], array[i]
    return array

def selectionSort(array):
    lenghtArray = len(array)
    for i in range(lenghtArray):
        minElement = i
        for j in range(i + 1, lenghtArray):
            if array[j] < array[minElement]:
                minElement = j
        array[i], array[minElement] = array[minElement], array[i]
    return array

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
    if lenghtArray > 1:
        mid = lenghtArray // 2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array
    
def quickSort(array):
    lengthArray = len(array)
    if lengthArray <= 1:
        return array
    else:
        pivot = array[0]
        left = [x for x in array[1:] if x <= pivot]
        right = [x for x in array[1:] if x > pivot]
        return quickSort(left) + [pivot] + quickSort(right)
    
array1 = [3,1,2]
array2 = [5,3,8,1,2]
array3 = [10,9,8,7,6,5,4,3,2,1]
array4 = [15,1,10,12,5,8,3,9,7,6,2,11,14,13,4]
array5 = [20,18,15,16,14,13,12,10,9,7,8,6,5,4,3,2,1,11,19,17]

#selectionSort(array3)
#insertionSort(array3)
print(array3)
quickSort(array3)
print(array3)