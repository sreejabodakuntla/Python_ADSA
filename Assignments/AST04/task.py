
def pair_sum_sorted_rotated(arr: list[int], target: int) -> bool:
    n = len(arr)
    if n < 2:
        return False

    # Find the pivot element (largest element)
    pivot = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            pivot = i
            break
            
    # l is index of smallest element, r is index of largest element
    r = pivot
    l = (pivot + 1) % n

    # Move pointers around the circular array
    while l != r:
        current_sum = arr[l] + arr[r]
        
        if current_sum == target:
            return True
        elif current_sum < target:
            l = (l + 1) % n  # Move to next larger element
        else:
            r = (r - 1 + n) % n  # Move to next smaller element

    return False