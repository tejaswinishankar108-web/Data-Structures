"""You are given an array of non-negative integers height which represent an elevation map. 
Each value height[i] represents the height of a bar, which has a width of 1.
Return the total amount of water that can be trapped between the bars."""

class Solution:
    def trap(self, height: list[int]) -> int:#defining a function that takes a list of integers as input and returns an integer representing the total amount of water that can be trapped between the bars.
        n = len(height)
        if n == 0:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        water_trapped = 0
        for i in range(n):
            water_trapped += min(left_max[i], right_max[i]) - height[i]

        return water_trapped

example = Solution()
print(example.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # Output: 6

#using stack: Time and space complexity is O(n) where n is the length of the height array, since we are using a stack to store the indices of the bars and iterating through the height array once.
class SolutionStack:
    def trap(self, height: list[int]) -> int:
        stack = []
        water_trapped = 0
        n = len(height)

        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[top]
                water_trapped += distance * bounded_height
            stack.append(i)

        return water_trapped