# Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
#
# Example 1:
#
# Input: [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [5, 2].
#
# Example 2:
#
# Input: [2, 1, 5, 2, 8], S=7
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [8].
#
# Example 3:
#
# Input: [3, 4, 1, 1, 6], S=8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to ‘8’ are [3, 4, 1] or [1, 1, 6].

def smallest_subarray(arr,k):
    minlen=len(arr)

    for i in range(len(arr)):
        j=i
        sum,sublen=0.0,0
        while(sum<k and j<len(arr)):
            sum=sum+arr[j]
            sublen+=1
            j+=1
        if(sum>=k):
            minlen=min(sublen,minlen)

    return minlen

def smallest_subarray_sum(s, nums):
    minLength=len(nums)+1
    winStart,winSum = 0,0.0
    length=0
    for i in range(len(nums)):
        winSum+=nums[i]
        length+=1
        while winSum >=s:
            if length<minLength:
                minLength=length
            winSum=winSum-nums[winStart]
            winStart=winStart+1;
            length-=1
    if(minLength>len(nums)):
        return -1
    return minLength

arr=[2, 1, 5, 2, 8]
k=7
print(smallest_subarray(arr,k))








