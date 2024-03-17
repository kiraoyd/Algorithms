#Imagine we have a board divided into 4 rows and 5 columns. There are pebbles scattered across the board, one per (row, columm) spot
#Pebbles exist at locations:  (0,0), (0,1), (1,1), (1,2),(1,3), (2,0), (2,3), (2,4), (3,0)
#There is a robot that starts at (0,0). It can move to the right or down.
#What is the max number of pebbles the robot can collect, if it traverses a legal path to (3,4)?
#----TABULAR SOLUTION---------#

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

#Function to traverse the 4 x 5 board and discover solution
#note: not written to be particularly flexible as it only works for a board of size 4x5
def pebble_tabular(board, row_start, column_start):
    #initialize table to all 0s, the flexible way
    #include and extra row and column to pad the table,
    table = []
    row_num = 4
    column_num = 5
    i = 0
    while(i < row_num) :
        temp = []
        c = 0
        while(c < column_num) :
            temp.append(0)
            c = c + 1
        table.append(temp)
        i = i + 1

    print("Initial table: ")
    print_matrix(table, 4, 5) #print the tables current state


    row = row_start
    column = column_start
    #traverse the board until we reach end square (3,4), take it one row at a time
    #We want to keep going as long as we still have a row to process, and stop when we are done with row 3
    while(row <= 3):
        column = column_start #reset column
        while(column <= 4):
            up =0
            behind = 0
            #only check above square, if it exists
            #otherwise just assume it to be 0, as initiatlized
            #this will prevent indexing the table out of bounds
            if(row > 0):
                up = table[row-1][column] #check the spot in the table above where we are
            if(column > 0):
                behind = table [row][column -1] #check the spot in the table behind( to the left) of where we are
            #get the max between the two
            max = up
            if(behind > max):
                max = behind

            #see if there is a pebble where we are
            pebble_here = board[row][column]

            #whats the solution for this spot at row,column on the board
            pebbles_collected = max + pebble_here

            #update table before moving on
            table[row][column] = pebbles_collected

            #print table to see progress
            print("The table after processing row ", row, " and column ", column, " is :")
            print_matrix(table, 4, 5) #print the tables current state

            #move one square to the right
            column += 1



        #when all columns in a row are processed, move to the next row down
        row +=1

    print("The final values in the table are:")
    print_matrix(table, 4,5) #print the tables current state

    #when all squares have been processed, row and column will be out of bounds by 1
    #reduce them each by one, to index to the table at the endpoint and get the solution
    return table[row-1][column-1]


#main calling routine

#initialize the 4 x 5 board with pebbles, the lazy non-flexible way
board = []

row1 = [1,1,0,0,0]
row2 = [0,1,1,1,0]
row3 = [0,0,0,1,1]
row4 = [1,0,0,0,0]

board.append(row1)
board.append(row2)
board.append(row3)
board.append(row4)

print("Board: ")
print_matrix(board, 4,5) #print the boards current state

start_row = 0
start_column = 0

max = pebble_tabular(board, start_row, start_column)

print("The max number of pebbles to be collected is: ", max)

