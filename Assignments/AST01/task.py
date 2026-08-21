

def The_Great_Run(N, K, arr):
    max_sum = sum(arr[:K])
    current_sum = max_sum

    for i in range(K, N):
        current_sum += arr[i] - arr[i - K]
        max_sum = max(max_sum, current_sum)

    return max_sum