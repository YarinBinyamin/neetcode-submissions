class Solution:
    def canJump(self, nums: List[int]) -> bool:
        seen = set()
        queue = deque([(0,nums[0])]) # (index, jump)
        while queue:
            index, length_jump = queue.pop()
            if index == len(nums) -1 :
                return True
            if index in seen:
                continue
            seen.add(index)
            length_jump = min(index+length_jump + 1, len(nums))
            for i in range(index+1, length_jump):
                queue.append((i,nums[i]))
        return False