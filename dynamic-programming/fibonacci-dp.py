# reference: https://medium.com/@davidguandev/introduction-to-dynamic-programming-with-examples-bc04dca3ccee

memo = {}
def fibonacci_dp(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        f = 1
    else:
        f = fibonacci_dp(n-1) + fibonacci_dp(n-2)
    memo[n] = f
    return f
    