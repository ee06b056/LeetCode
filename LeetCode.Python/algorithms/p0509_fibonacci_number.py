class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        fib_list = [0, 1]
        for i in range(2, n + 1):
            a, b = fib_list[-1], fib_list[-2]
            fib_list.append(a + b)
        return fib_list[-1]
    
    def fib_optimized(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b