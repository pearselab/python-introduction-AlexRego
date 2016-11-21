## Bubble sort
def bubblesort(nums):
    for n in range(len(nums)-1, 0, -1):
        for i in range(n):
            if nums[i] < nums[i+1]:
                nums[i], nums[i +1] = nums[i+1], nums[i]
    return nums

## Quick sort
def quicksort(nums):
    bottom = 0
    top = len(nums)

## Partition
def partition(list, bottom, top):
    pivot = nums[top]
    x = bottom
    for i in range(bottom,top-1):
        if nums[i] < pivot:
            nums[i], nums[bottom] = nums[bottom], nums[i]
            x += 1
    return x
