def zeros_to_the_right(arr):
    non_zeros = []
    zeros = []
    for i in arr:
        if i == 0:
            zeros.append(0)
        else:
            non_zeros.append(i)

    return non_zeros + zeros


print(zeros_to_the_right([0, 3, 1, 0, -2]))