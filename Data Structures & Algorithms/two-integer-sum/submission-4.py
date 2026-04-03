class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap ={}
        for i,v in enumerate(nums):
            new_val = target - v
            if new_val not in hashmap :
                hashmap[v]=i
            else:
                return [hashmap[new_val],i]
        return [-1,-1]
        