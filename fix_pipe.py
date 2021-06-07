'''Issue
Looks like some hoodlum plumber and his brother has been running around and damaging your stages again.

The pipes connecting your level's stages together need to be fixed before you receive any more complaints. Each pipe should be connecting, since the levels ascend, you can assume every number in the sequence after the first index will be greater than the previous and that there will be no duplicates.

Task
Given the a list of numbers, return the list so that the values increment by 1 for each index up to the maximum value.

Example
Input: 1,3,5,6,7,8

Output: 1,2,3,4,5,6,7,8'''

def pipe_fix(nums):
    i=0
    max=0
    while i<len(nums):
        if nums[i]>max:
            max=nums[i]
        i=i+1
    j=nums[0]
    list1=[]
    while j<=max:
        list1.append(j)
        j=j+1
    return list1
nums=[1,4,7,3,8,12]
print(pipe_fix(nums))