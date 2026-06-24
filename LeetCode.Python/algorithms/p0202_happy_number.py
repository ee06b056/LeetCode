class Solution:
    def isHappy(self, n: int) -> bool:
        def Next(n: int) -> int:
            next_n = 0
            while n > 0:
                next_n += (n % 10) ** 2
                n //= 10
            return next_n
        seen = set()
        while n != 1:
            if n in seen:
                return False
            else:
                seen.add(n)
            n = Next(n)
        return True
    
    def isHappy(self, n: int) -> bool:
        def Next(n: int) -> int:
            next_n = 0
            while n > 0:
                next_n += (n % 10) ** 2
                n //= 10
            return next_n
        if n == 1:
            return True
        slow = Next(n)
        fast = Next(Next(n))
        while slow != fast:
            slow = Next(slow)
            fast = Next(Next(fast))
        return slow == 1