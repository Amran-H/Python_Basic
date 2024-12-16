nums = [2,7,11,15]
target = 9


# for a in range(0, len(nums)):
#     for b in range(a+1, len(nums)):
#         if nums[a]+nums[b] == target:
#             print([a,b])
#             break
    
for b in range(0, len(nums)):
    a = target - nums[b]
    if a in nums and b != nums.index(a):
        print([b, nums.index(a)])
        break