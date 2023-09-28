class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        right -= 1
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        left += 1

        ans = list(ans)
        for k in range(len(ans)):
            ans[k] = list(ans[k])

        return ans



sol = Solution()
print(sol.fourSum([1,0,-1,0,-2,2], 0))