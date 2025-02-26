def intersection(nums1,nums2):
    nums1.sort() # Sorting the first array
    nums2.sort() # sorting the second array
    N=len(nums1) # take the some values
    M=len(nums2)
    p1=0
    p2=0
    intersection=set() # taking an intersection set .
    while p1<N and p2<M:  
        if nums1[p1]==nums2[p2]: # add the values to the set if values at both pointers are equal
            intersection.add(nums1[p1])
            p1+=1
            p2+=1
        elif nums1[p1]<nums2[p2]:
            p1+=1
        else:
            p2+=1
    result=[] # taking an other array / list
    for i in intersection:
        result.append(i)
    # return the result
    return result

print("The Intersection of the two arrays : ")
nums1=[4,9]
nums2=[9,4,6,2]
r=intersection(nums1,nums2)
print(r)