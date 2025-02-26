def moveZeros(nums):
    l=0
    for i in range(1,len(nums)):
        if nums[i]!=0:
            nums[l], nums[i] = nums[i], nums[l]
            l+=1
    return nums
# def moveZeros(nums):
#     l=0
#     for i in range(len(nums)):
#         if nums[i]!=0:
#             nums[i],nums[l]=nums[l],nums[i]
#             l+=1
#     return nums

nums=[0,1,0,3,12]
res=moveZeros(nums)
print(res)

