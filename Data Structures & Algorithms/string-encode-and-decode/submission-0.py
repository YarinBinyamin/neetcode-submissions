class Solution:

    def encode(self, strs: List[str]) -> str:
        to_send = ""
        for e in strs:
            for c in e:
                new_c = chr((ord(c)+1) % 256)
                to_send +=new_c
            to_send += chr(21) # space
        return to_send

    def decode(self, s: str) -> List[str]:
            ans =[]
            cur_str = ""
            for c in s:
                c_numrical = (ord(c)-1) % 256
                if c_numrical == 20:
                    ans.append(cur_str)
                    cur_str=""
                else:
                    cur_str+= chr(c_numrical)
            return ans