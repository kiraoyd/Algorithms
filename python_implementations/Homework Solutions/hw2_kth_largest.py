def quicksort(array, start, end):
    #basecase
    if start >= end:
        #We have a one element array, it is sorted already
        return

    #Place the pivot using partition, and get back it's final resting location (this will be the mid value we split the array on)
    mid = partition(array, start, end)

    #mid at this point, is in it's correct sorted spot, it doesn't ever need to move again
    #so don't include it in either sub array
    #recursive call to sort the right hand sub array
    quicksort(array, mid+1, end)
    #recursive call to sort the left hand sub array
    quicksort(array, start, mid-1)


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

def find_kth_largest(array, k):
    start = 0
    end = len(array) - 1
    quicksort(array, start, end)
    return array[end-k] #kth largest will be at the end-k index in the now sorted array


#-------MAIN CALLING ROUTINE------#
array = [8,9,2,10,1,3]
size = len(array) - 1

k= 3
kth_largest = find_kth_largest(array, k)

print(f"If k is {k}, then the kth largest element is: {kth_largest}")

