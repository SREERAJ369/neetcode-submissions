class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker_dict = {}
        for i in strs:
            sorted_word = "".join(sorted(i))
            if sorted_word in tracker_dict:
                tracker_dict[sorted_word].append(i)
            else:
                tracker_dict[sorted_word] = [i]
        result = []
        for group in tracker_dict:
            result.append(tracker_dict[group])
        return result
        