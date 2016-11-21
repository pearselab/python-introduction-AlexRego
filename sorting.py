## Bubble sort
def bubblesort(nums):
    for n in range(len(nums), 0, -1):
        for i in range(n):
            if nums[i] < nums[i+1]:
                nums[i], nums[index +1] = nums[i+1], nums[i]
    return nums

## Quick sort
def quicksort(nums, bottom, top)
