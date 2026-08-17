"""Using arrays to find the product of all elements in an array."""

def product_except_self(nums):
    n = len(nums)
    answer = [1] * n#defining the answer array with 1s, as the product of an empty set is 1.
    #for example, if the input array is [1, 2, 3, 4], answer will be initialized as [1, 1, 1, 1].
    # Calculate prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
        #prefix is updated to be the product of all elements before the current index. 
        #For example, after processing the first element (1), prefix becomes 1. 
        # After processing the second element (2), prefix becomes 2, and so on. 
        # This way, answer[i] will hold the product of all elements before index i.

    # Calculate postfix products and multiply with prefix products
    postfix = 1
    for i in range(n - 1, -1, -1):#initializing range to iterate backwards through the array,
        #starting from the last index (n - 1) down to the first index (0).
        answer[i] *= postfix
        postfix *= nums[i]

    return answer

print(product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
"""Showing step by step calculation for the input [1, 2, 3, 4]:
1. Initialize answer array: [1, 1, 1, 1]
2. Calculate prefix products:
   - i = 0: answer[0] = 1, prefix = 1 * 1 = 1
   - i = 1: answer[1] = 1, prefix = 1 * 2 = 2
   - i = 2: answer[2] = 2, prefix = 2 * 3 = 6
   - i = 3: answer[3] = 6, prefix = 6 * 4 = 24
   Resulting answer array after prefix calculation: [1, 1, 2, 6]
   3. Calculate postfix products:
   - i = 3: answer[3] = 6 * 1 = 6, postfix = 1 * 4 = 4
   - i = 2: answer[2] = 2 * 4 = 8, postfix = 4 * 3 = 12
   - i = 1: answer[1] = 1 * 12 = 12, postfix = 12 * 2 = 24
   - i = 0: answer[0] = 1 * 24 = 24, postfix = 24 * 1 = 24
   Resulting answer array after postfix calculation: [24, 12, 8, 6]
   Final answer array: [24, 12, 8, 6]"""

