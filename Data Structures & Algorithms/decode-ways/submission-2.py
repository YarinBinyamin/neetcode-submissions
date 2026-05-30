class Solution:
    def numDecodings(self, s: str) -> int:
        memo ={}
        def rec(res ):
            #memo
            if res in memo:
                return memo[res]
            
            #stopping condition
            if len(res) == 0 : 
                return 1
            
            if res[0] == '0':
                return 0
            ways = 0

            # take 2 digits first
            if len(res) >= 2 and 10 <= int(res[:2]) <= 26:
                ways += rec(res[2:])

            # take 1 digit second
            ways += rec(res[1:])

            memo[res] = ways
            return ways

        return rec(s)