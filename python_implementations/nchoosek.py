#Non-dynamic version, runs in exponential time O(2^n)
def n_choose(n, k):
    #BASE CASES:
    # for n choose k where k is exactly 1, the answer will always be n
    if k == 1:
        return n
    #for n choose k where n == k, the answer always be 1
    if n == k:
        return 1

    #Have a couple of kids to solve my subproblems for me
    return n_choose(n-1, k-1) + n_choose(n-1, k) #sum their solutions together to get my own


#Dynamic Programming version, uses Memoization, runs in linear time O(n)
def n_choose_memo(n,k,table):
    #check the table storing our solutions first to see if I even need to do any work:
    if table[n][k] != -1:
        #its been solved hurrah!
        return table[n][k] #send back the solution

    #Otherwise, it hasn't been solved, so I need to do the work:
    #BASE CASES:
    if k == 1:
        return n
    if n == k:
        return 1

    #Have a couple of kids to solve my subproblems for me
    result = n_choose_memo(n-1, k-1, table) + n_choose_memo(n-1, k, table)
    table[n][k] = result #if I did the work, I better save my solution into the table so other kids don't have to do the same work
    return result #then I can return my solution

#---------------MAIN CALLING ROUTINE-------------------------#
#On these inputs, the non-dynamic version will run SUUUPER slow
#But the dynamic programming version should finish running within a second or too
n = 40
k = 17

#table to store the solutions as we solve the subproblems:
table = [[-1] *(k+1) for _ in range(n+1)] #build table initialized with -1's
print(n_choose_memo(n, k, table)) #Call the dynamic programming version
#print(n_choose(n,k)) #call the non-dynamic version