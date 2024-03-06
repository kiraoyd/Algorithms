
#Here we find the value of the kth largest element within quicksort itself
#We can cut our recursive input size in half each time, and potentially exist quicksort much earlier
def quicksort_find_kth(array, start, end, k_index):
    #basecase
    if start >= end:
        #We have a one element array, it is sorted already
        return array[start]

    #Place the pivot using partition, and get back it's final resting location (this will be the mid value we split the array on)
    mid = partition(array, start, end)
    if mid == k_index:
        #we've successfully placed the pivot, and it is now in the kth largest spot, no need to continue sorting
        return array[mid]

    #mid at this point, is in it's correct sorted spot, it doesn't ever need to move again
    #so don't include it in either sub array
    #only continue searching on the relevant half of the subarray
    if mid < k_index:
        #kth largest element must end up being placed in the upperhalf of the sorted array
        #recursive call to sort the right hand sub array
        return quicksort_find_kth(array, mid+1, end, k_index)
    else:
        #kth largest element must end up being placed in the lower half of the sorted array
        #recursive call to sort the left hand sub array
        return quicksort_find_kth(array, start, mid-1, k_index)


def partition(array, start, end):
    pivot_val = array[end] #assume the pivot val is the last element in the array

    #set a tracker index to move through and process every element
    index = start #it begins at the start of this array, and moves to the end

    #set a placeholder for the spot one to the right of the elements that are less than the pivot value
    #This placeholder starts at the start of the array, if we find an element smaller than the pivot, we put it in the placeholders spot, and then increment the placeholder to the next spot
    placeholder = start

    #As long as the index tracker has non-pivot values to process, keep going
    while index < end:
        #if the element index is on, is less that the pivot, we want to swap it to the placeholders spot
        #NOTE: if an element is a pivot duplicate, it skips the swap step and that leaves the duplicates placed just before the pivot, which is fine and where they should be
        if array[index] < pivot_val:
            temp = array[placeholder]
            array[placeholder] = array[index]
            array[index] = temp

            #and now after the swap, the placeholder is pointing at something smaller than the pivot value, so we increment it
            placeholder += 1

        #keep moving index forward to process all elements other than the pivot
        index += 1


    #once index has finished checking every element against the pivot, all that's left is
    #to swap the value at the placeholder with the pivot value itself
    #The placeholder was holding the spot just to the right of all the smaller-than-pivot values we placed
    #so this is the correct spot for the pivot to go
    array[end] = array[placeholder]
    array[placeholder] = pivot_val

    #the partition is complete, return the placeholder which indicates the location of the pivot
    return placeholder


#-------MAIN CALLING ROUTINE------#
array = [8,9,2,10,1,3]
last_index = len(array) - 1

k= 1
index = len(array) - k #transform k into the index where it will be located (the 1st largest element lives in the last index)
kth_largest = quicksort_find_kth(array, 0, last_index, index)


print(f"If k is {k}, then the kth largest element is: {kth_largest}")
