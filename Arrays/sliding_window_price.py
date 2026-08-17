"""You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day."""
"""You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0."""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:#defining a function that takes a list of integers as input and returns an integer representing the maximum profit that can be achieved by buying and selling NeetCoin.
        min_price = float('inf')  # Initialize min_price to a very large value
        max_profit = 0  # Initialize max_profit to 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update min_price if a lower price is found
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update max_profit if a higher profit is found

        return max_profit

example = Solution()
print(example.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5