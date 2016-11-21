## Bubble sort
def bubblesort(nums):
    for n in range(len(nums), 0, -1):
        for i in range(n):
            if nums[i] < nums[i+1]:
                nums[i], nums[i +1] = nums[i+1], nums[i]
    return nums

## Quick sort
def quicksort(nums):
    bottom = 0
    top = len(nums)

## Partition
def partition(list):
    bottom = 0
    top = len(nums)
    pivot = nums[top]
