class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
            memo = [[None for _ in range(amount+1)] for _ in range(len(coins))]
            def rec (index, a ):
                if a == amount:
                    return 1
                if index >= len(coins) or a > amount:
                    return 0
                if memo[index][a] is not None:
                    return memo[index][a]
                if coins[index] > amount - a:
                    memo[index][a] = rec(index+1,a)
                else:
                    memo[index][a] = rec(index+1,a) + rec(index, a +coins[index])
                return memo[index][a]
            return rec(0,0) 
        