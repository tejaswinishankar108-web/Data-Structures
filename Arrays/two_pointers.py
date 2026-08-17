class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr = newStr + c.lower()
        return newStr == newStr[::-1] #will return true or false
"""The space complecity is O(n) because we are creating a new string to store the alphanumeric characters in lowercase. 
The time complexity is O(n) where n is the length of the string, since we are iterating through the string once to create
 the new string and then checking if it is a palindrome."""

#using two pointers technique to check if the string is a palindrome
#time complexity is O(n) where n is the length of the string, 
#since we are iterating through the string once to check if it is a palindrome.
#space complexity is O(1) because we are not using any extra space to store the characters in the string.
class Solution2Pointers:
    def isPalindrome(self, s: str) -> bool:#defining a function that takes a string as input and returns a boolean value indicating whether the string is a palindrome or not.
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.alphanumeric(s[left]):
                #checking if the character at the left pointer is not alphanumeric, 
                # if it is not, we move the left pointer to the right.
                left += 1
            while left < right and not self.alphanumeric(s[right]):
                #checking if the character at the right pointer is not alphanumeric, 
                # if it is not, we move the right pointer to the left.
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def alphanumeric(self, c: str) -> bool:
        #defining a helper function that checks if a character is alphanumeric (i.e., a letter or a digit).
        #ord is a built-in function in Python that returns the Unicode code point for a given character.
        #uni code means a unique number assigned to each character in the Unicode character set.
        return (ord('A')<=ord(c)<=ord('Z')) or(ord('a')<=ord(c)<=ord('z')) or (ord('0')<=ord(c)<=ord('9'))
example1 = Solution()
print(example1.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
example2 = Solution2Pointers()  
print(example2.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True