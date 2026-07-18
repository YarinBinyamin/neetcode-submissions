class Solution:
    def reorganizeString(self, s: str) -> str:
        count_letters = Counter(s)
        n = len(s)
        if max(count_letters.values()) > (n+1) //2:
            return ""
        
        ans = [""] * n
        index = 0 
        
        for char, freq in count_letters.most_common():
            for _ in range(freq):
                ans[index] = char
                index+=2
                
                if index >= n:
                        index = 1
        
        return "".join(ans)