class Activity: 
    def fibonnacci(self):
        print("You selected Fibonacci Sequence Program \n")
        terms = int(input("Please input the number of terms: "))
        first = 0
        second = 1
        print(first, second, end=" ")
        for count in range(2, terms):
            c = first + second
            print(c, end=" ")
            first = second
            second = c
        print("")
run1 = Activity()
run1.fibonnacci()
run2 = Activity()
run2.fibonnacci()