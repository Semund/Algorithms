from random import randint


def insertion_sort(nums):
    for i in range(1, len(nums)):
        item = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item
    return nums


if __name__ == '__main__':
    print(insertion_sort([randint(1, 100) for _ in range(100)]))
