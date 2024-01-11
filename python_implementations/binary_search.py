#BINARY SEARCH: iterative, in-place (no extra data structures needed) solution

#Given a 1d array of 'n' number of positive integers SORTED in ascending order, and some target integer k
#Determine if k exists in the array.
#If k exists, return the index location where it can be found.
#If k does not exist, return the fail flag of -1
#Note - pythons array type is called a List
import math
def find_k_binary(sorted, k, size):
    start = 0
    end = size - 1
    #We must also check the situation where start equals end, to check the value of the last element remaining
    while start <= end:
        #mid represents the index location of the value in the array we want to check against the value of k
        mid = math.floor((start + end) / 2) #python converts to a float on integer divide, so we must floor it
        if sorted[mid] == k:
            #We found k, return the index location
            return mid
        #shrink the window of data we examine in the array
        if k > sorted[mid]:
            #we know k must be in the right half, if it exists, and we can 'throw out' the left half
            start = mid + 1
            #end is unchanged, as it still points at the correct 'upper end' of the new window of data
        if k < sorted[mid]:
            #we know k will be in the left half, if it exists, and we can 'throw out' the right half
            end = mid - 1
            #start is unchanged, as it still points at the correct 'lower end' of the new window of data

    #If we have processed all data and not found k, return the fail to find flag of -1
    return -1


#Test: to run - python3 binary_search.py
array = [1,2,3,4,6]
start = 0
size = len(array)
result = find_k_binary(array, 2, size)
print(result)



