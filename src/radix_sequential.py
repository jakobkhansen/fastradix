from utils import fill_prefix_sum, get_digit, get_num_digits


def radixsort(array : list[int]):
    if len(array) <= 1:
        return array.copy()

    n = len(array)

    input = array.copy()
    output = [0]*n


    max_num_digits = get_num_digits(max(array, key=abs))

    for i in range(max_num_digits):
        count = [0]*10
        for elem in input:
            digit = get_digit(elem, i)
            count[digit] += 1
        fill_prefix_sum(count)
        for elem in input:
            digit = get_digit(elem, i)
            index = count[digit]
            output[index] = elem
            count[digit] += 1
        input,output = output,input

    # If negative numbers
    positive_index = n-1
    negative_index = 0

    for elem in reversed(input):
        if elem < 0:
            output[negative_index] = elem
            negative_index += 1
        else:
            output[positive_index] = elem
            positive_index -= 1

    input,output = output,input

    return input

