
import sys

def is_palindrome(s: str, left: int, right: int) -> bool:
    """Helper to check if substring s[left:right+1] forms a palindrome."""
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def Check_Palindrome(n: int, s: str) -> bool:
    left, right = 0, n - 1
    
    while left < right:
        if s[left] != s[right]:
            # Try skipping the character at left OR right
            return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
        left += 1
        right -= 1
        
    return True

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if len(input_data) >= 2:
        n = int(input_data[0])
        s = input_data[1]
        print(Check_Palindrome(n, s))