class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    	n = len(nums)
		current_index = 1
		for i in range(1, n):
			if nums[i] != nums[i-1]:
				nums[current_index] = nums[i]
				current_index += 1
			else:
				continue
		return current_index 



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_index = 1
        nums[current_index-1] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[current_index] = nums[i]
                current_index += 1
            else:
                continue
        return current_index