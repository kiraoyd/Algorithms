import math

def least_exact_greedy(n):
    quarters = math.floor(n/25) #how many quarters can we grab?
    pennies_left = n - (quarters * 25) #subtract that amount from n

    dimes = math.floor(pennies_left/10) #how many dimes can we grab out of the remainder?
    pennies_left = pennies_left - (dimes * 10) #subtract that amount from the remainder

    nickels = math.floor(pennies_left/5)
    pennies_left = pennies_left - (nickels * 5)

    #penny count will be the final value in pennies_left

    print(f"Quarters: {quarters}, Dimes: {dimes}, Nickels: {nickels}, Pennies: {pennies_left}")
    least_change = quarters+dimes+nickels+pennies_left
    print("result: ", least_change)

#works assuming we get the coins available in a list, sorted in descending order
def lec_greedy_list(n, coins):
    total_coins = 0
    change = []

    index = 0
    while index < len(coins):
        #for each coin value, try to extract as many as possible
        while n >= coins[index]:
            #We can still grab the largest value of coin
            n -= coins[index] #grab the coin, removing its value from n
            change.append(coins[index]) #add that coin to our list of coins grabbed
            total_coins += 1 #tally up the coin count
        #once we've exghausted the larger coin value, move onto the smaller
        index += 1

    print(f"The least exact change given is: {change}, for a total coin count of: {total_coins}.")


#-----MAIN CALLING ROUTINE-----#
n = 100
least_exact_greedy(n)

coins = [25, 10, 5, 1]
lec_greedy_list(n, coins)