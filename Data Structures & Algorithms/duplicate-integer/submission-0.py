class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        original_set = set()
        for i in nums:
            if i not in original_set:
                original_set.add(i)
            else:
                return True
        return False