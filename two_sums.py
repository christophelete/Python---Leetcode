class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dicto = dict()
        for idx, num in enumerate(nums):
            if target - num not in dicto:
                dicto[num] = idx
            else:
                return [dicto[target - num], idx]
