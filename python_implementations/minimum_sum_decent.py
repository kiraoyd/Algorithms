#Kira Klingenberg
#Minimum Sum Decent - Tabulation Solution

# diagnostic print tool, used to nicely print any matric of size m x n
def print_matrix(mat,m,n) :
    r = 0
    while(r < m) :
        c = 0
        while(c < n) :
            print(mat[r][c], end=" ")
            c = c + 1
        print()
        r = r + 1
    print()

def min_sum(t,n):

    #table starts out holding the initial problem, but the code here will
    #process and update to the same table (saves a little bit of memory)

    r = n - 2  #start at the 2nd to last row (we need one row below us to query)

    #we will traverse the table starting from the bottom row, moving left to right across columns
    while(r >=0):
        #each row starts with a value for the column at 0
        c = 0
        while(c <= r):
            a = t[r+1][c] #below me
            b = t[r+1][c+1] #below and to the right of me

            #find minimum between two options
            min = a
            if(b < a):
                min = b

            #update the existing table with the value stored where I am, and the min of the two things below me
            t[r][c] = t[r][c] + min

            #see the table at each step:
            print(f"The min sum decent from row {r} column {c} to the base is: {t[r][c]}, and the updated table looks like: ")
            print_matrix(t, n, n)

            #move to process the next spot to the right
            c = c+1
        #move to process the next row up
        r = r -1

    return t[0][0]


#---------MAIN CALLING ROUTINE-----------#

#example matrix holding the data for this problem
table = []
#Apex of this example triangle is 2
row0 = [2,0,0,0]
row1= [7,4,0,0]
row2=[1,8,5,0]
row3 = [10,1,40,6]

table.append(row0)
table.append(row1)
table.append(row2)
table.append(row3)

n = 4
print("The initial table looks like this: ")
print_matrix(table, n, n)

print("The minimum sum decent is to move from 2 --> 7 --> 1 --> 1, for a total minimum sum of 11. Lets see it in action: ")
print("\n")

min_sum_decent = min_sum(table, n)
print(f"After tabulating we can grab the value stored at (0,0), which now holds the min_sum decent solution of: {min_sum_decent}")