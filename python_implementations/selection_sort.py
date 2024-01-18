
#Selection sort implemented with a single data structure, where 'array' represents the unsorted 1d array
#and 'n' represents the size of array
def selection_sort_inplace(array, n):
    start = 0
    while start < n: #go until start has checked all the items in the list
        index = start + 1 #walk the array to find the minimum, from start to end
        min = start #first unsorted item
        while index < n:
            if array[index] < array[min]:
                min = index #save the minimum seen's location
            index += 1
        #swap
        temp = array[start]
        array[start] = array[min]
        array[min] = temp
        #move start forward to do it all again
        start += 1
