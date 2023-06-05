###Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.


nums = [0, 1, 0, 3, 12]

ans = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[i], nums[ans] = nums[ans], nums[i]
        ans += 1

print(nums)
