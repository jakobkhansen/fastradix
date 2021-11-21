import math

def successfully_sorted(original : list[int], permutation : list[int]):
    return is_permutation(original, permutation) and is_sorted(permutation)

def is_sorted(a : list[int]):
    return not any([True  if a[i] < a[i-1] else False for i in range(1,len(a))])

def is_permutation(original : list[int], permutation : list[int]):
    original_counts = get_counts(original)
    permutation_counts = get_counts(permutation)

    return original_counts == permutation_counts

def get_counts(a : list[int]):
    counts = {}
    for i in a:
        counts[i] = counts.get(i, 0) + 1
    return counts

def fill_prefix_sum(a : list[int]):
    sum = 0
    for i,e in enumerate(a):
        a[i] = sum
        sum += e
    return a

def get_digit(number, n):
    return number // 10**n % 10

def get_num_digits(number):
    return int(math.log10(number) + 1)
