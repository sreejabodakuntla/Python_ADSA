
def product_except_self(arr: list[int]) -> list[int]:
    n = len(arr)
    if n == 0:
        return []

    res = [1] * n

    # Step 1: Calculate prefix products
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= arr[i]

    # Step 2: Calculate suffix products and combine with prefix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= arr[i]

    return res

if __name__ == '__main__':
    # Example usage / test
    import sys
    input_data = sys.stdin.read().split()
    if input_data:
        arr = [int(x) for x in input_data]
        print(product_except_self(arr))