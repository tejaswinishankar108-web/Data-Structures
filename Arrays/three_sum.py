"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, 
and the indices i, j and k are all distinct."""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:#defining a function that takes a list of integers as input 
        #and returns a list of lists of integers representing the triplets that add up to zero.
        nums.sort()  # Sort the array to use two pointers technique
        result = []  # Initialize an empty list to store the triplets

        for i in range(len(nums) - 2):#-2 because we need at least three numbers to form a triplet
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values for the first number
                continue

            left, right = i + 1, len(nums) - 1  # Initialize two pointers
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]  # Calculate the sum of the triplet
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])  # Add the triplet to the result
                    while left < right and nums[left] == nums[left + 1]:  # Skip duplicates for the second number
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # Skip duplicates for the third number
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1  # Move the left pointer to increase the sum
                else:
                    right -= 1  # Move the right pointer to decrease the sum

        return result

example = Solution()
print(example.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
