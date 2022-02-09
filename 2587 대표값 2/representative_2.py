# BOJ 2587 대표값 2

def median(arr):
    return sorted(arr)[2]


def average(arr):
    return sum(arr) // 5


nums = [int(input()) for _ in range(5)]
print(average(nums))
print(median(nums))
