
def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def Check_Palindrome(n, s):
    left = 0
    right = n - 1

    while left < right:
        if s[left] != s[right]:
            return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)

        left += 1
        right -= 1

    return True


n = int(input())
s = input()

print(Check_Palindrome(n, s))