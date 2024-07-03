import tkinter as tk
from tkinter import ttk

class SortingAlgorithms():
    def __init__(self,array,sortAlgo):
        self.array = array
        self.sortAlgo = sortAlgo

    def bubbleSort(self,array):
        lenghtArray = len(array)
        for i in range(0, lenghtArray):
            for j in range(i + 1, lenghtArray):
                if array[i] >= array[j]:
                    array[i], array[j] = array[j], array[i]
        return array
    
    def selectionSort(self,array):
        lenghtArray = len(array)
        for i in range(lenghtArray):
            minElement = i
            for j in range(i + 1, lenghtArray):
                if array[j] < array[minElement]:
                    minElement = j
            array[i], array[minElement] = array[minElement], array[i]
        return array
    
    def insertionSort(self,array):
        lenghtArray = len(array)
        for i in range(1, lenghtArray):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j+1] = array[j]
                j -= 1
            array[j + 1] = key
        return array
    
    def mergeSort(self,array):
        lenghtArray = len(array)
        if lenghtArray > 1:
            mid = lenghtArray // 2
            left = array[:mid]
            right = array[mid:]

            self.mergeSort(left)
            self.mergeSort(right)

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
    
    def quickSort(self,array):
        lengthArray = len(array)
        if lengthArray <= 1:
            return array
        else:
            pivot = array[0]
            left = [x for x in array[1:] if x < pivot]
            right = [x for x in array[1:] if x > pivot]
            return self.quickSort(left) + [pivot] + self.quickSort(right)
            
    def selectedSort(self):
        match self.sortAlgo:
            case "bubble":
                return self.bubbleSort(self.array)
            case "selection":
                return self.selectionSort(self.array)
            case "insertion":
                return self.insertionSort(self.array)
            case "merge":
                return self.mergeSort(self.array)
            case "quick":
                return self.quickSort(self.array)

class SortingApp:
    def __init__(self, root, array_1, array_2, array_3, array_4, array_5):
        self.root = root
        self.array_1 = array_1
        self.array_2 = array_2
        self.array_3 = array_3
        self.array_4 = array_4
        self.array_5 = array_5
        self.root.geometry("500x200")
        self.root.title("Sorting Method")

        label = tk.Label(root, text="Sorting Method", font=('Arial', 25))
        label.pack(padx=20, pady=20)

        start_button = tk.Button(root, text="Start", font=('Arial', 35), command=self.open_menu_window)
        start_button.pack(pady=20)

    def open_menu_window(self):
        menu_window = tk.Toplevel(self.root)
        menu_window.title("Menu Options")
        menu_window.geometry("300x450")

        label = tk.Label(menu_window, text="Select Sorting Method", font=('Arial', 22))
        label.pack(pady=20)

        buttonframe = tk.Frame(menu_window)
        buttonframe.pack(fill='y')

        buttonframe.columnconfigure(0, weight=1)

        b1 = tk.Button(buttonframe, text="Bubble Sort", font=('Arial', 20), command= lambda: self.open_array_window("bubble"))
        b1.grid(row=0, column=0, sticky=tk.W+tk.E)

        b2 = tk.Button(buttonframe, text="Selection Sort", font=('Arial', 20), command= lambda: self.open_array_window("selection"))
        b2.grid(row=1, column=0, sticky=tk.W+tk.E)

        b3 = tk.Button(buttonframe, text="Insertion Sort", font=('Arial', 20), command= lambda: self.open_array_window("insertion"))
        b3.grid(row=2, column=0, sticky=tk.W+tk.E)

        b4 = tk.Button(buttonframe, text="Merge Sort", font=('Arial', 20), command= lambda: self.open_array_window("merge"))
        b4.grid(row=3, column=0, sticky=tk.W+tk.E)

        b5 = tk.Button(buttonframe, text="Quick Sort", font=('Arial', 20), command= lambda: self.open_array_window("quick"))
        b5.grid(row=4, column=0, sticky=tk.W+tk.E)

        b6 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=menu_window.destroy)
        b6.grid(row=5, column=0, sticky=tk.W+tk.E)

    def open_array_window(self,sortAlgo):
        array_window = tk.Toplevel(self.root)
        array_window.title("Array Lists")
        array_window.geometry("300x450")

        label = tk.Label(array_window, text="Select Array Lists", font=('Arial', 22))
        label.pack(pady=20)

        buttonframe = tk.Frame(array_window)
        buttonframe.pack(fill='y')

        buttonframe.columnconfigure(0, weight=1)

        button1 = tk.Button(buttonframe, text="Array 1", font=('Arial', 20), command=lambda: self.array_window(sortAlgo, self.array_1, "Array 1"))
        button1.grid(row=0, column=0, sticky=tk.W+tk.E)

        button2 = tk.Button(buttonframe, text="Array 2", font=('Arial', 20), command=lambda: self.array_window(sortAlgo, self.array_2, "Array 2"))
        button2.grid(row=1, column=0, sticky=tk.W+tk.E)

        button3 = tk.Button(buttonframe, text="Array 3", font=('Arial', 20), command=lambda: self.array_window(sortAlgo, self.array_3, "Array 3"))
        button3.grid(row=2, column=0, sticky=tk.W+tk.E)

        button4 = tk.Button(buttonframe, text="Array 4", font=('Arial', 20), command=lambda: self.array_window(sortAlgo, self.array_4, "Array 4"))
        button4.grid(row=3, column=0, sticky=tk.W+tk.E)

        button5 = tk.Button(buttonframe, text="Array 5", font=('Arial', 20), command=lambda: self.array_window(sortAlgo, self.array_5, "Array 5"))
        button5.grid(row=4, column=0, sticky=tk.W+tk.E)

        button6 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=array_window.destroy)
        button6.grid(row=6, column=0, sticky=tk.W+tk.E)

    def array_window(self,sortAlgo,array,name):
        unsorted_array5_window = tk.Toplevel(self.root)
        unsorted_array5_window.title(name)
        unsorted_array5_window.geometry("950x400")

        label = tk.Label(unsorted_array5_window, text=f"Array: {array}", font=('Arial', 22))
        label.pack(pady=20)

        label = tk.Label(unsorted_array5_window, text="Sort Array?", font=('Arial', 22))
        label.pack(pady=30)

        buttonframe = tk.Frame(unsorted_array5_window)
        buttonframe.pack(fill='y')

        buttonframe.columnconfigure(0, weight=1)

        b1 = tk.Button(buttonframe, text="Yes", font=('Arial', 20), command= lambda: self.sorted_window(sortAlgo,array,name))
        b1.grid(row=0, column=0, sticky=tk.W+tk.E)

        b2 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=unsorted_array5_window.destroy)
        b2.grid(row=1, column=0, sticky=tk.W+tk.E)

    def sorted_window(self,sortAlgo,array,name):
        sorted_array5_window = tk.Toplevel(self.root)
        sorted_array5_window.title(name)
        sorted_array5_window.geometry("950x400")

        sorting = SortingAlgorithms(array,sortAlgo)
        array = sorting.selectedSort()

        label = tk.Label(sorted_array5_window, text="Sorted Array", font=('Arial', 22))
        label.pack(pady=20)

        label = tk.Label(sorted_array5_window, text= array, font=('Arial', 22))
        label.pack(pady=30)

        buttonframe = tk.Frame(sorted_array5_window)
        buttonframe.pack(fill='y')

        buttonframe.columnconfigure(0, weight=1)

        back_button5 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=sorted_array5_window.destroy)
        back_button5.grid(row=1, column=0, sticky=tk.W+tk.E)

array1 = [3,1,2]
array2 = [5,3,8,1,2]
array3 = [10,9,8,7,6,5,4,3,2,1]
array4 = [15,1,10,12,5,8,3,9,7,6,2,11,14,13,4]
array5 = [20,18,15,16,14,13,12,10,9,7,8,6,5,4,3,2,1,11,19,17]


if __name__ == "__main__":
    root = tk.Tk()
    app = SortingApp(root, array1, array2, array3, array4, array5)
    root.mainloop()
