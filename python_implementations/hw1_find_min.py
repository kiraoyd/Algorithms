#-----------------------------------------------------------------------------------------------#
#We don't know what the minimum value itself IS, so all we can do is try to figure out which side of the array it will be on
#The approach here is to draw out all possible rotations for a toy (small example) input array
#Split these possibilities into two groups: those where the minimum value falls in the left sub array, and those where it falls in the right. We consider the middle value to be part of the left subarray.
#Using the values we DO know (start, end and we can calculate mid), are there any consistent relationships between them in either case?
#What we'll find is that, in every example case where the minimum falls on the right, array[mid] is greater than array[end]
#And in every example case where the minimum falls on the left, array[mid] is less than or equal to array[end]
#We can use this information to run a check on every subarray to whittle down the values until all we have left is the minimum
#----------------------------------------------------------------------------------------------------#
import math
def min_rotated(rotated, size):
    if size == 0:
        return -1 #empty array error flag

    start = 0 #points to the element all the way on the left
    end = size -1  #points to the element all the way to the right

    #BEST CASE: the array is rotated n-times, back to its original state
    #We can then find the minimum value in constant time (skipping the loop that's dependent on n)
    if rotated[start] < rotated[end]:
        #The array is already in min to max sorted order
        return rotated[start] #so the minimum is the first value

    #Every iteation, determine if the minimum val will be on the left or right subarray
    while start < end: #go until start == end, indicating a single element subarray
        mid = math.floor((start+end) / 2)
        #the following check deduced from examplifying all rotations of a toy example array
        if rotated[mid] > rotated[end]:
            #When this is true, the pivot is guaranteed to be in the right subarray, so throw out the left
            start = mid + 1
        else:
            #The pivot is guaranteed to be in the left subarray (we count the array[mid] value as part of the left sub array), so throw out the right
            end = mid #We keep the value at array[mid], it is considered to be part of the left subarray

    #When the loop breaks, start and end point at the same element, and the subarry is just one element
    return rotated[start] 	#This will be the minimum value we have been searching for

