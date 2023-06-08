def fibonacci_recursive(n):
    if n <= 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
        
def fibonacci_loop(n):
    if n <= 0 :
        return 
    elif n == 1 :
        return 1

    fib_sequence = [0, 1]
    for i in range(2, n + 1) :
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    return fib_sequence[n]
                
def fibonacci_memoization(n, memo = {}) :
    if n <= 0 :
        return 0
    elif n == 1 :
        return 1

    if n in memo :
        return memo[n]
    else :
        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
        return memo[n]
                        
n = input()

print(fibonacci_recursive(n))     
print(fibonacci_loop(n))           
print(fibonacci_memoization(n))    
