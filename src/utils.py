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



