class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,v in enumerate(nums):
            k=target-v
            if k in hashmap:
                return [hashmap[k],i]
            hashmap[v]=i