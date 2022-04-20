# Given an array, find the average of all
# subarrays of ‘K’ contiguous elements in it.

def avgOfSubarrOfK(K,arr):
    result=[]
    for i in range(len(arr)-K+1):
        sum=0.0
        for j in range(i,i+K):
            sum=sum+arr[j]
        result.append(sum/K)
    return result

def avgOfSubOfKWindow(K,arr):
    result=[]
    winStart=arr[0]
    winSum=0.0
    j=0
    for i in range(len(arr)):
        winSum = winSum+arr[i]
        j+=1
        if(j==K):
            result.append(winSum/K)
            winSum=winSum-winStart
            j-=1
            winStart=arr[i-K+2]
    return result

def avgOfSubofWinSolv(K,arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]  # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if windowEnd >= K - 1:
            result.append(windowSum / K)  # calculate the average
            windowSum -= arr[windowStart]  # subtract the element going out
            windowStart += 1  # slide the window ahead

    return result

arr=[1, 3, 2, 6, -1, 4, 1, 8, 2]
print(avgOfSubarrOfK(5,arr))
print(avgOfSubOfKWindow(5,arr))




