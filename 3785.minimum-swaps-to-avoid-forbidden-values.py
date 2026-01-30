class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)
        swap_count = 0
        for i in range(n):
            if nums[i] == forbidden[i]:
                for j in range(n):
                    if nums[j] != forbidden[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        swap_count += 1
                        break
                else:
                    return -1  # No valid swap found
        return swap_count