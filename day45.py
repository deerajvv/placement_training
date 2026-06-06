class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = []
        count = 0
        count1 = 0
        for i in range(len(nums)):
            if nums[i] == target:
                n.append(i)
                count += 1
                break

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                n.append(i)
                count1 += 1
                break

        if count == 0 and count1 == 0:
            n.append(-1)
            n.append(-1)
        return n