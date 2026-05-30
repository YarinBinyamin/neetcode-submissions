class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = len(t)
        my_dic = Counter(t)

        left, right = 0, 0
        min_window_size = float("inf")
        min_window_str = ""

        n = len(s)

        while right < n:
            c = s[right]

            if my_dic[c] > 0:
                need -= 1

            my_dic[c] -= 1
            right += 1

            while need == 0:
                window_size = right - left

                if window_size < min_window_size:
                    min_window_size = window_size
                    min_window_str = s[left:right]

                left_char = s[left]
                my_dic[left_char] += 1

                if my_dic[left_char] > 0:
                    need += 1

                left += 1

        return min_window_str