class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        ans = []
        left,right = 0 , 0 
        seen = set()
        sum =0
        while right < len(s):
            seen.add(s[right])
            count[s[right]] -=1
            sum +=1
            if count[s[right]] == 0:
                seen.remove(s[right])
            if not seen:
                ans.append(sum)
                sum =0
            right+=1
        return ans