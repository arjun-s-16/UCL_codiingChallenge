#Question 1
#Checking for exploitable arbitrage oppurtunities

'''
ALGORITHM:

The idea is to assign values to products (say in dollars using first column of matrix) and checking in other columns for a mismatch in the exchange rates.  
'''

#CODE: 

# Exchange rate matrix of size 3*3 which is symmetric
exchange_rate_matrix = [
    [1, 2, 3],
    [1.0 / 2, 1, 3.0 / 2],
    [1.0 / 3, 2.0 / 3, 1]
]

#Initial cost of n products calculated by assuming value of product 1 as $1 
initial_cost = [1, 1.0 / 2, 1.0 / 3]

arbitrage_opportunities = False

#Traversing remaining exchange rates (upper half of matrix since it is symmetric)
for i in range(3):
    for j in range(i + 1, 3):
        new_cost = exchange_rate_matrix[i][j] * initial_cost[j]
        if new_cost != initial_cost[i]:
            print("Arbitrage opportunities are available")
            arbitrage_opportunities = True
            exit(0)

print("No arbitrage opportunities available")

#END OF CODE


'''
Time complexity analysis:
    Exchange matrix is traversed only once. Hence 
    T(n) = O(n*n);
    
Space Complexity:
    O(n*n);
'''
