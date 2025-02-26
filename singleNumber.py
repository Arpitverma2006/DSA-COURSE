def singleNumber(nums):
    res=0
    for num in nums:
        res^=num
    return res

nums=[2,2,1]
r=singleNumber(nums)
print(r)