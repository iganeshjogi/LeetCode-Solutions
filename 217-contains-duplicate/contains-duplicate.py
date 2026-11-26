class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        frequency = {}

        for i in nums:

            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1


        for i in frequency:

            if frequency[i] > 1:
                return True
    
        return False