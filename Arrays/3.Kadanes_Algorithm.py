class Kadane:
    """
    A class containing methods to solve the maximum subarray problem.
    """
    
    def max_subarray_sum(self, nums: list[int]) -> int:
        """
        Finds the maximum sum of a contiguous subarray using Kadane's Algorithm.
        
        Args:
            nums: A list of integers.
            
        Returns:
            The maximum subarray sum.
        """
        # Edge case: return 0 if the input list is empty
        if not nums:
            return 0

        # Initialize tracking variables with the first element
        max_sum = nums[0]
        current_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Decision: Add current number to the existing chain, or start a new chain?
            current_sum = max(num, current_sum + num)
            
            # Update the global maximum if the current chain is larger
            max_sum = max(max_sum, current_sum)
            
        return max_sum


# The block below allows the script to run directly inside VS Code
if __name__ == "__main__":
    # 1. Create an instance of the class
    calculator = Kadane()
    
    # 2. Define a test array
    test_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    
    # 3. Call the class method and store the result
    result = calculator.max_subarray_sum(test_array)
    
    # 4. Print the output to the VS Code terminal
    print(f"The input array is: {test_array}")
    print(f"The maximum subarray sum is: {result}")

#the time complexity of Kadane's Algorithm is O(n), where n is the number of elements in the input array.
# This is because we traverse the array only once, performing constant-time operations for each element. 
# The space complexity is O(1) since we use a fixed amount of space regardless of the input size.