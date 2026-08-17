"""Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target 
and index1 < index2. 
Note that index1 and index2 cannot be equal, therefore you may not use the same element twice."""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:#defining a function that takes a list of integers 
        #and a target integer as input and returns a list of two integers representing the indices of the two numbers 
        # that add up to the target.
        left, right = 0, len(numbers) - 1  # Initialize two pointers

        while left < right:
            current_sum = numbers[left] + numbers[right]  # Calculate the sum of the two pointers
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-indexed positions
            elif current_sum < target:
                left += 1  # Move the left pointer to the right to increase the sum
            else:
                right -= 1  # Move the right pointer to the left to decrease the sum

        return []  # Return an empty list if no solution is found

example = Solution()
print(example.twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]
