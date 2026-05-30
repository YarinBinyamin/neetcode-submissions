class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        end =0
        start =0
        dic = {}
        max_length = 1
        while end < len(s):
            dic[s[end]] = dic.get(s[end],0) +1
            biggest_char = max(dic.values())
            if (end - start +1) - biggest_char <= k :
                max_length = max (max_length , end -start +1)
            else : 
                while (end - start +1) - biggest_char > k and start < end:
                    dic[s[start]] = dic.get(s[start],0) -1
                    start +=1
                max_length = max (max_length , end -start +1)
            end +=1
        return max_length