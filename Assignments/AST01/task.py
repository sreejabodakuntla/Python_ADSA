
def pair_sum_sorted_rotated(arr, target):
    n = len(arr)

    if n < 2:
        return False

    pivot = 0

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            pivot = i
            break

    l = (pivot + 1) % n
    r = pivot

    while l != r:
        current_sum = arr[l] + arr[r]

        if current_sum == target:
            return True
        elif current_sum < target:
            l = (l + 1) % n
        else:
            r = (r - 1 + n) % n

    return False


n = int(input())
arr = list(map(int, input().split()))
target = int(input())

print(pair_sum_sorted_rotated(arr, target))