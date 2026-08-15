
import sys

def max_girls_impressed(N: int, K: int, girls: list[int]) -> int:
    # Calculate the sum of the first window of size K
    current_sum = sum(girls[:K])
    max_sum = current_sum
    
    # Slide the window across the array
    for i in range(K, N):
        current_sum += girls[i] - girls[i - K]
        max_sum = max(max_sum, current_sum)
        
    return max_sum

if __name__ == '__main__':
    # Reading input from standard input
    input_data = sys.stdin.read().split()
    if input_data:
        N = int(input_data[0])
        K = int(input_data[1])
        girls = [int(x) for x in input_data[2:2 + N]]
        
        print(max_girls_impressed(N, K, girls))