class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
            memo = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
            def rec(i,val):
                if val == 0:
                    return 0
                if i >= len(coins) or val < 0:
                    return float("inf")
                if memo[i][val] != -1:
                    return memo[i][val]
                else:
                    memo[i][val] = min(1+ rec(i,val - coins[i]), rec(i+1,val ))
                return memo[i][val]
            ans = rec(0,amount)
            return -1 if ans == float("inf") else ans    