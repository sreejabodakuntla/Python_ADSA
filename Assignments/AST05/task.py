
def productExceptSelf(arr):
    n = len(arr)

    if n == 0:
        return []

    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= arr[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= arr[i]

    return result