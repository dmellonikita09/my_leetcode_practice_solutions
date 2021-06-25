import random
class Solution:

    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        nums2 = list(self.array)
        for index in range(len(self.array)):
            r_index = random.randrange(len(nums2))
            self.array[index] = nums2.pop(r_index)
        return self.array
        


# Your Solution object will be instantiated and called as such:
nums = [[[1,2,3]],[],[],[]]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()

