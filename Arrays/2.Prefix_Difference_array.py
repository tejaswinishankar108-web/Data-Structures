class PrefixSum:
    """
    A class to handle efficient Range Sum Queries using the Prefix Sum technique.
    Time Complexity:
        - Construction: O(N)
        - Range Sum Query: O(1)
    Space Complexity: O(N) to store the prefix array.
    """
    def __init__(self, arr):
        self.arr = arr
        n = len(arr)
        # Create a prefix array padded with an extra 0 at the beginning 
        # to handle queries starting at index 0 seamlessly.
        self.prefix = [0] * (n + 1)
        
        for i in range(n):
            self.prefix[i + 1] = self.prefix[i] + arr[i]

    def query(self, left: int, right: int) -> int:
        """
        Returns the sum of elements from index 'left' to 'right' (inclusive).
        Bound checks are assumed to be handled by the caller.
        """
        # Sum(L, R) = Prefix[R + 1] - Prefix[L]
        return self.prefix[right + 1] - self.prefix[left]

class DifferenceArray:
    """
    A class to handle efficient Range Updates using the Difference Array technique.
    Time Complexity:
        - Construction: O(N)
        - Range Update: O(1)
        - Reconstructing Final Array: O(N)
    Space Complexity: O(N) to store the difference array.
    """
    def __init__(self, arr):
        self.original_length = len(arr)
        # Create a difference array. We allocate size N + 1 to easily 
        # handle updates where the right index is the last element of the array.
        self.diff = [0] * (self.original_length + 1)
        
        if self.original_length > 0:
            self.diff[0] = arr[0]
            for i in range(1, self.original_length):
                self.diff[i] = arr[i] - arr[i - 1]

    def update(self, left: int, right: int, val: int) -> None:
        """
        Adds 'val' to all elements in the range from index 'left' to 'right' (inclusive).
        """
        #difference array technique: we add val to the left index and subtract val from the right index + 1.
        self.diff[left] += val
        if right + 1 < self.original_length:
            self.diff[right + 1] -= val
            """
            Step-by-Step Walkthrough
            Imagine we start with an array of six zeros, 
            meaning our difference array is also all zeros:
            diff = [0, 0, 0, 0, 0, 0]
            We call update(left=1, right=3, val=5) 
            (we want to add 5 to indices 1, 2, and 3):
            self.diff[1] += 5
            The array becomes: [0, 5, 0, 0, 0, 0]
            self.diff[3 + 1] -= 5 (which is index 4)
            The array becomes: [0, 5, 0, 0, -5, 0]
            How it resolves during reconstruction:
            When you call get_final_array(), 
            it calculates the running prefix sum of this diff array from left to right:
            Index 0: 0Index 1: 0 + 5 = 5 (The increment starts)
            Index 2: 5 + 0 = 5
            Index 3: 5 + 0 = 5
            Index 4: 5 + (-5) = 0 (The increment is cancelled out here)
            Index 5: 0 + 0 = 0
            Final reconstructed array: [0, 5, 5, 5, 0, 0]"""

    def get_final_array(self) -> list:
        """
        Reconstructs and returns the updated array by taking the prefix sum 
        of the difference array.
        """
        final_arr = [0] * self.original_length
        if self.original_length == 0:
            return final_arr

        running_sum = 0
        for i in range(self.original_length):
            running_sum += self.diff[i]
            final_arr[i] = running_sum
            
        return final_arr


# --- Demonstration and Testing ---
def main():
    # Original array from the explanation
    original_array = [3, 1, 4, 1, 5, 9]
    print(f"Original Array: {original_array}\n")

    # ==========================================
    # 1. Prefix Sum Demonstration
    # ==========================================
    print("--- 1. Prefix Sum Demonstration ---")
    ps = PrefixSum(original_array)
    print(f"Constructed Prefix Array (padded): {ps.prefix}")
    
    # Query: Sum from index 2 to 4 (values: 4 + 1 + 5 = 10)
    L, R = 2, 4
    result_sum = ps.query(L, R)
    print(f"Range Sum Query ({L} to {R}): {result_sum} (Expected: 10)")
    
    # Query: Sum from index 0 to 3 (values: 3 + 1 + 4 + 1 = 9)
    L2, R2 = 0, 3
    result_sum2 = ps.query(L2, R2)
    print(f"Range Sum Query ({L2} to {R2}): {result_sum2} (Expected: 9)\n")

    # ==========================================
    # 2. Difference Array Demonstration
    # ==========================================
    print("--- 2. Difference Array Demonstration ---")
    da = DifferenceArray(original_array)
    print(f"Initial Difference Array: {da.diff}")
    
    # Perform Range Updates
    # Update 1: Add 5 to indices 1 to 3
    print("\nApplying Update: Add +5 to range [1, 3]")
    da.update(1, 3, 5)
    print(f"Difference Array after Update 1: {da.diff}")
    
    # Update 2: Add -2 to indices 3 to 5
    print("Applying Update: Add -2 to range [3, 5]")
    da.update(3, 5, -2)
    print(f"Difference Array after Update 2: {da.diff}")
    
    # Reconstruct the final updated array
    updated_array = da.get_final_array()
    print(f"\nFinal Reconstructed Array: {updated_array}")
    
    # Manual verification math:
    # Index 0: 3                              -> 3
    # Index 1: 1 + 5                          -> 6
    # Index 2: 4 + 5                          -> 9
    # Index 3: 1 + 5 - 2                      -> 4
    # Index 4: 5 - 2                          -> 3
    # Index 5: 9 - 2                          -> 7
    print("Expected Final Array:      [3, 6, 9, 4, 3, 7]")


if __name__ == "__main__":
    main()
