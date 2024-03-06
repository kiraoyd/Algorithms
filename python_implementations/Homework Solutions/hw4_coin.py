#Assume n is the total number of cents we need to make with our coins
#We have three different coin denominations:
# A 1-cent coin
# A 3-cents coin
# A four-cents coin
# What's the smallest number of coins we can gather up to reach a total of 'n' cents?

def least_change_memo(n, table):
    if table[n] != -1:
        return table[n]
    if n <= 0: #On the last grab, we tried to grab more cents than we have room to add, grabbing any more coins will give us a total over n
        return 0
    if n == 1: #After grabbing the last coin, we have room fo exactly 1-cent, and can grab a single coin
        return 1
    if n == 3: #After grabbing the last coin, we have room for exactly 3-cents, and can grab a single coin
        return 1
    if n == 4: #After grabbing the last coin, we have room for exactly 4-cents, and can grab a single coin
        return 1

    #solve this for the three possible situations:

    #We grab a 4-cent coin, taking 4 cents away from n
    four = least_change_memo(n-4, table)
    #We grab a 3-cent coin, taking 3 cents away from n
    three = least_change_memo(n-3, table)
    #We grab a 1-cent coin, taking 1 cent away from n
    one = least_change_memo(n-1, table)

    #If we got here in the first place, we must have grabbed a coin, so add that 1+ coin to the minimum of what our kids figure out
    result = 1 + min(four, three, one)

    table[n] = result
    return result

def least_change_tab(n, table):
    if n == 0:
        return 0 #no total means no coins
    if n == 1 or n == 3 or n == 4:
        return 1

    size = len(table)

    #set base cases
    table[0] = 0
    table[1] = 1
    table[3] = 1
    table[4] = 1

    #we can start with n = 2 as our smallest unsolved subproblem
    index = 2
    while index < size: #we want to process the last element as that represents n
        if index - 4 >= 0: # we can consider all previous coin denominations
            table[index] = 1 + min(table[index-4], table [index-3], table[index-1])
        elif index - 3 >= 0: #we can consider only the 1 and 3 coin denominations
            table[index] = 1 + min(table[index-3], table[index-1])
        else: #we can only consider picking up the 1-cent coin
            table[index] = 1 + table[index-1]

        index += 1

    return table[index - 1]



#------MAIN CALLING ROUTINE------#


n = 30
table = [-1] * (n+1)  #make and initialize using pythons list comprehension
#assume we just won't use index 0 for anything in our memo table, to keep our indicies in range.
result = least_change_memo(n, table)
print(f"The result of solving this with memoization is: {result}")

tabs = [-1 for _ in range(n)]  #another way to create the table with list comprehension
result2 = least_change_tab(n, tabs)
print(f"The result of solving this with tabulation is: {result2}")