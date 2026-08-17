"""Sliding window pattern is a technique for solving problems that involve arrays or lists. 
It involves creating a "window" of a fixed size that moves through the array, 
allowing you to efficiently calculate values based on the elements within that window."""

def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return -1  # Not enough elements for the window size

    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    window_sum = sum(arr[:k])  # Calculate the sum of the first window
    max_sum = max(max_sum, window_sum)  # Update max_sum if needed

    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]  # Slide the window: add new element, remove old element
        max_sum = max(max_sum, window_sum)  # Update max_sum if needed
        #priting the values that return the maximum sum of the subarray of size k.
        #printing only the values that return the maximum sum of the subarray of size k.
        
    return max_sum


print(max_sum_subarray([2,1, 5, 2, 3, 4, 5, 3, 9, 1, 7, 8], 3))  # Output: 17
