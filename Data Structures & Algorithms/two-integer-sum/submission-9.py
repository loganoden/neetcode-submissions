class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Assume there exists one exact solution
        # Dict to store numbers we've seen and their original indicies
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            # If the complement exists in our dict, we found the pair
            if complement in seen:
                # seen[complement] was added earlier, so it'll be the smaller index
                return [seen[complement], i]
            
            # Otherwise, add the current number and its index to the dict
            seen[num] = i