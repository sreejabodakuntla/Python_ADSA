
import sys

def count_good_substrings(s: str) -> int:
    count = 0
    n = len(s)
    
    # Check every window of length 3
    for i in range(n - 2):
        a, b, c = s[i], s[i+1], s[i+2]
        if a != b and b != c and a != c:
            count += 1
            
    return count

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        s = input_data[0]
        print(count_good_substrings(s))