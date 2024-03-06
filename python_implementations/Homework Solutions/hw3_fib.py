#Standard Recursive fibonacci
def fib(n):
    if n <= 0: #0th fib number is 0
        return 0
    if n == 1: #first fib number is 1
        return 1
    return fib(n-1) + fib(n-2)


def fib_memo(n, table):
    #first check the table
    if table[n] >= 0:
        return table[n]
    if n <= 0:
            return 0
    if n == 1:
        return 1
    result = fib(n-1) + fib(n-2)
    table[n] = result #add the newly solved value to the table
    return result



#------MAIN CALLING ROUTINE-------#
n = 8
table = [-1] * (n+1)  #make an array of size n + 1 to hold solutions to all fib numbers
print(table)
result = fib_memo(n, table)
print(f"If n is {n}, then the nth fibonacci number is: {result}")