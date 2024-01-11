#LINEAR SEARCH: iterative, in-place (no extra data structures needed) solution

#Given some unsorted 1d array with a given size n, containing unique positive integers, and some target integer k
#Determine if k exists in the array.
#If k exists, return the index location where it can be found.
#If k does not exist, return the fail flag of -1
#Note pythons array type is called a List
def find_k(array, k, n):
    if n == 0: #edge case: array is empty, k cannot exist in it
        return -1
    if k < 0: #the array contains only positive values, so if k is negative it cannot be in the array
        return -1
    index = 0
    #Starting at index 1, walk the array
    while index < n:
        #compare each value against the value for k
        if array[index] == k:
            #if the value at the current index is equivalent to k, we found it and return that index
            return index
        index += 1 #if no match has been found, continue to walk the array

    #If we complete the loop and are still in the function, we failed to find k
    return -1

