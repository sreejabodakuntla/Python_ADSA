
def pairInSortedRotated(arr, target):
    n = len(arr)

    # Find the position where rotation happens
    i = 0
    while i < n - 1 and arr[i] <= arr[i + 1]:
        i += 1

    left = (i + 1) % n
    right = i

    while left != right:
        if arr[left] + arr[right] == target:
            return True

        if arr[left] + arr[right] < target:
            left = (left + 1) % n
        else:
            right = (right - 1 + n) % n

    return False