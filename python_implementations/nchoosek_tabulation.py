
def initialize_table(table, n, k):
    #populate base cases
    row_max = n
    col = 0 #just populating column 0 with base case results of 1
    row = 0
    while row <= row_max:
        table[row][col] = 1
        row += 1

    #starting at 0,0 populate all row == col elements with base case results of 1
    col_max = k
    row = 0
    col = 0
    #break when we run out of columns (the value of k will be less than n)
    while col <= col_max:
        table[row][col] = 1
        row += 1
        col += 1

#I asked chatGPT how to make the table output pretty in python:
def print_table(table):
    for row in table:
        print(" ".join(map(str, row)))

def nchoosek_tab(table, n, k):
    if n == k:
        return 1
    if k == 1:
        return 1
    #smallest subproblem always starts at 2 choose 1 for n choose k, as long as we alrady populated the base cases
    result = 0
    col = 1
    while col <= k:
        row = 2
        while row <= n:
            #add the previous sub problems results together
            #store into current spot on table
            table[row][col] = table[row-1][col-1] + table[row-1][col]
            row += 1 #process all data in one column first, top to bottom
        col += 1 #then move to the next column

    return table[row-1][col-1] #row and col go one outside the table bounds, so print the last values before that happens and this is the result to the larger probelem




#-------------MAIN-------------#
#NOTE: I wanted to break this up into more functions, but ran into issues with how Python passes lists by reference and had to give it up for the sake of time
print("Welcome to the n choose k problem! Type '1' to continue, '0' to quit: ")
choice = int(input())
while choice != 0:
    if choice < 0 or choice > 1:
        print("That wasn't a valid selection, please try again.")
    else:
        n = int(input("Please enter the value for 'n':"))
        k = int(input("Please enter the value for 'k': "))

        #As long as we have a valid k and n values
        if k <= n and k > 0 and n > 0:
            #short-code to build the table intialized with 0's:
            table = [[0] *(k+1) for _ in range(n+1)]

            #Show the tables if we have a non base case
            if k != 1 and k != n:
                print(f"The table before initialization is: ")
                print_table(table)
                initialize_table(table, n, k)
                print(f"The table after initialization is: ")
                print_table(table)

            #this function handle the base cases so we can call it either way
            result = nchoosek_tab(table, n, k)

            #only want to show a table if we had to run tabulation at all (non base case)
            if k != 1 and k != n:
                print(f"The table after we tabulate is: ")
                print_table(table)

            print(f"\n{n} choose {k} is: {result}\n")

        elif k == 0:
            print(f"\n{n} choose {k} is: 1.\n There is only one way to NOT place any of {n} things. \n")

        else:
            print("That's not a valid n choose k problem.")

    #get another menu choice
    choice = int(input("Type '1' to continue, '0' to quit: "))