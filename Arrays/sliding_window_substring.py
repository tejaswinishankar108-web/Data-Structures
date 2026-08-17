"""You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters."""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:#defining a function that takes two strings as input and 
        #returns a boolean value indicating whether s2 contains a permutation of s1.
        from collections import Counter
        #collections is a built-in Python module that provides alternatives to Python's general-purpose built-in containers 
        # like dict, list, set, and tuple.
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False

        count_s1 = Counter(s1)
        #defining a variable count_s1 that stores the frequency of each character in s1 using the Counter class 
        # from the collections module.
        count_window = Counter(s2[:len_s1]) #defining a variable count_window that stores the frequency of each character
        #in the first len_s1 characters of s2 using the Counter class from the collections module.

        if count_s1 == count_window:
            return True

        #sliding window technique to check if any substring of s2 has the same character frequency as s1
        for i in range(len_s1, len_s2):
            count_window[s2[i]] += 1#incrementing the count of the character at index i in s2 in the count_window dictionary.
            count_window[s2[i - len_s1]] -= 1#decrementing the count of the character at index i - len_s1 in s2 in the count_window dictionary.

            if count_window[s2[i - len_s1]] == 0:#checking if the count of the character at index i - 
                #len_s1 in s2 is zero in the count_window dictionary.
                del count_window[s2[i - len_s1]]#deleting the character at index i - len_s1 in s2 from the count_window dictionary if its count is zero.

            if count_s1 == count_window:#checking if the character frequency of s1 is equal to the character frequency of the current window in s2.
                return True

        return False