class Solution:
    def removeDuplicates(self, nums) -> int:
        prev = 0
        index = 0
        for i in range(len(nums)):
            if index >= len(nums):
                break
            if i == 0:
                prev = nums[i]
                index = 1
                pass
            else:
                if nums[index] == prev:
                    nums.pop(index)
                else:
                    prev = nums[index]
                    index += 1

        print(nums)
        return len(nums)


sol = Solution()
arr = [1,1]
sol.removeDuplicates(arr)

