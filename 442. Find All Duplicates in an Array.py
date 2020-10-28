# 

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        return [ x for x in count if count[x]==2]
        