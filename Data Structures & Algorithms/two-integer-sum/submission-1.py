class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker_dict = {}
        for index,value in enumerate(nums):
            complement = target - value
            if complement in tracker_dict:
                return [tracker_dict[complement], index]
            else:
                tracker_dict[value] = index
