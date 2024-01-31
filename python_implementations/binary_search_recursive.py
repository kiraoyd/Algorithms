import math

#Searches for k in a sorted array of integers
#Returns the index at which k is found, if it is found
#Returns -1 if k is not found
def binary_search_recursive(sorted, k, start, end):
    mid = math.floor((start + end) / 2)
    #Base case: found k at sorted[mid]
    if sorted[mid] == k:
        return mid
    #Base case: we've gone past the single element situation and not fouond k, time to return the error flag
    if start > end:
        return -1

    #Same check as the iterative version, if k is greater than the mid value, we want to check the right subarray
    if k > sorted[mid]:
        start = mid + 1
        return binary_search_recursive(sorted, k, start, end)
    #If k is less than the mid value, we want to check the left subarray
    if k < sorted[mid]:
        end = mid - 1
        return binary_search_recursive(sorted, k, start, end)