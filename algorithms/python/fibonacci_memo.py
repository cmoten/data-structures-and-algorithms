def fib(n: int, memo: dict = {})->int:
    if n in memo.keys():
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

def main():
    print(fib(50))
    print(fib(60))
    print(fib(100))
    
if __name__ == '__main__':
    main()