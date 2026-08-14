
arr=[2,3,4,5,6]
target=11
found =False
left,right=0,len(arr)-1
while left<right:
    if arr[left]+arr[right]==target:
        found=True
        print("Pair found at index",left,"and",right)
        break
    elif arr[left]+arr[right]<target:
        left+=1
    else:
        right-=1
if not found:
    print("Pair not found")