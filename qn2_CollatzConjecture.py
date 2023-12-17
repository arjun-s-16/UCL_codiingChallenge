
#Question 2 
#Proving Collatz conjecture for first n natural numbers

'''
Algorithm:

The idea is to check using naive approach for numbers from 1 to n. And in this process store the previously computed results in an array (dynamic programming concept) to avoid repeated computations
'''

#CODE:

def util(num, array):
    #Returning true assuming the conjecture is true for numbers above 100000 and for previously computed results.
    if num >= len(array) or array[num]:
        return True
        
    #Base Case
    if num == 1:
        return True
    ans = False
    if num % 2 == 0:
        ans = util(num // 2, array)
    else:
        ans = util(num * 3 + 1, array)
        
    #Storing computed result
    if ans and num < len(array):
        array[num] = True
    return ans

def main():
    print("Enter n to prove Collatz conjecture for first n natural numbers :")
    n = int(input())

    #DP array which stores true for number i if Collatz conjecture is proved for number i earlier.
    #Assuming 1 lakh as maximum number and proving conjecture before it.
    array = [False] * (100000 + 1)
    array[1] = True
    
    for i in range(1, n + 1):
        if not array[i]:
            util(i, array)

    for i in range(1, n + 1):
        if not array[i]:
            print("Collatz conjecture is not true for number ", i)

    print("Collatz conjecture is proved")

if __name__ == "__main__":
    main()
    
#END OF CODE   

'''
Time complexity analysis:
Each number from 1 to 100000 (assumed here) is checked for conjecture property and the recursive function is called only once. Hence T(n) = O(n)

Space Complexity: 
    O(100000) = O(1) 
'''