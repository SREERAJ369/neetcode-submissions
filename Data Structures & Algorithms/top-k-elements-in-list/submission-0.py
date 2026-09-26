class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency_dict = {}
        # for i in nums:
        #     if i in frequency_dict:
        #         frequency_dict[i]+=1
        #     else:
        #         frequency_dict[i] = 1

        frequency_dict = Counter(nums)
        
        sorted_dict = dict(sorted(frequency_dict.items(),key= lambda x:x[1], reverse = True))
        return list(sorted_dict.keys())[0:k]
