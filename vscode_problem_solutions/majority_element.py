class Solution:
    def majority_element(nums):
        n = []                  #To store count of each elements
        for x in nums:
            count = 0
            for i in range(len(nums)):
                if x == nums[i]:
                    count+=1
            n.append(count)
        a = max(n)              #largest in counts list
        for i in range(len(n)):
            if n[i] == a:
                return nums[i]  #element,frequency
        return
    nums = [2,2,1,1,1,2,2]
    print(majority_element(nums))