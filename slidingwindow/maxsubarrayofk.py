#Given an array of positive numbers and a positive number ‘k,’
#
# find the maximum sum of any contiguous subarray of size ‘k’.

# Example 1:
#
# Input: [2, 1, 5, 1, 3, 2], k=3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Example 2:
#
# Input: [2, 3, 4, 1, 5], k=2
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

def max_sub_array_of_size_k(k, arr):
    maxsum=0.0

    for i in range(len(arr)-k):
        sum=0.0
        for j in range(i,i+k):
            sum=sum+arr[j]
        if(sum>maxsum):
            maxsum=sum
    return maxsum

def maxsubarraywindow(k,arr):
    maxsum=0.0
    wstart=arr[0]
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]
        if(i>=k-1):
            if(maxsum<sum):
                maxsum=sum
            wstart=arr[i-k+1]
            sum=sum-wstart
    return maxsum


arr=[2, 1, 5, 1, 3, 2]
k=3
# print(max_sub_array_of_size_k(k,arr))
print(maxsubarraywindow(k,arr))


arr=[2, 3, 4, 1, 5]
k=2
# print(max_sub_array_of_size_k(k,arr))
print(maxsubarraywindow(k,arr))






