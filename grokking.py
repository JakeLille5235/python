# algorithms from Grokking to practice / write myself to understand

# BIG O NOTATION ...
# to calculate (all logs are base2), ln(n)/ln(2) = # of run-times

# helpful functions for demonstration / learning purposes...
# print array (view sorting)
def printArray(array):
    for x in array:
        print(str([x]))

# binary search , O(log n)

# example array list (sorted, necessary for binary search)
exList = ["ABBY", "AZZY", "DORK", "JORDAN", "XELO", "ZACHARY"]
def binarySearch(list, item):
    low = 0 # all indexes start at 0
    high = len(list)-1 # since index starts at 0, length - 1 = last index

    while low <= high:
        mid = int((low+high)/2) # indicies MUST be integers (not floats, as / 2 might create)
        guess = list[mid]
        if guess == item:
            print("Located at " + str(mid))  # return the middle element (index) as this is where the guess is stored
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    print("No Matches for " + str(item) + ".")        
    return None

binarySearch(exList, "AZZY")

# simple sort (find smallest) - requires TWO functions (find smallest, sort/make list)
# slow, in-effective but understand the principle... O(n^2) runtime

testArray2 = [1, 135, 4, 5,83,7,156,5, 14, 561 , 43, 15, 1501, 523, 136 , 624]
def findSmallest(array):
    smallest = array[0]
    smallest_index =  0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

# slow, in-efficient, but works
def selectionSort(array):
    newArray = [] # init new array to store smallest values as found
    for i in range(len(array)): # for loop to iterate and find smallest values, "range(len(array))" creates sequence to go through entire array, useful for finding index, modifying elements, iterate array
        smallest = findSmallest(array) # function call
        newArray.append(array.pop(smallest)) # append the newArray to add values IN order
    return newArray # return pointer to new array in memory

#sortedArray = selectionSort(testArray2)
#for i in range(len(sortedArray)):
#    print(sortedArray[i])


# quick sort, aka. "divide and conquer"
def quick_sort(array):
    # base case, the "final" case that ends function
    if len(array) < 2:
        return array
    
    # pivot point (essential, used to compare, arbitrary just pick 1)
    pivot = array[int(len(array)/2)] # this picks the first element as the pivot point to compare in linear time

    # partition into two lists: less than or greater/equal to pivot (we join them after, pivot in center)
    less_than_pivot = [x for x in array[1:] if x < pivot]

    
    greater_or_equal_pivot = [x for x in array[1:] if x >= pivot]

    # recursive (call until complete) + combine
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_or_equal_pivot)


sortedArray = quick_sort(testArray2)
printArray(sortedArray)


