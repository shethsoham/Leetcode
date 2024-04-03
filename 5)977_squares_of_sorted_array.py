class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
    
        res = [0] * len(nums)  # Pre-allocate space for the result list
        l, r = 0, len(nums) - 1  # Initialize two pointers

        # Iterate from the end of the result list to the beginning
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l] * nums[l]
                l += 1
            else:
                res[i] = nums[r] * nums[r]
                r -= 1

        return res