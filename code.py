def exercice2b(A):
    B = [0 for i in range(0, len(A))]
    for i in range(0, len(A)):
        count = 0
        for j in range(i+1, len(A)):
            if A[j] < A[i]:
                count += 1
        B[i] = count
    return B


def exercice2c(A):
    B = [0 for i in range(0, len(A))]
    non_zero_indexes = []
    negative_left_values = 0

    # count negative_left_values
    for i in range(0, len(A)):
        if A[i] < 0:
            negative_left_values += 1

    # manage all the cases where A[i] = 0
    for i in range(0, len(A)):
        if A[i] == 0:
            B[i] = negative_left_values
        if A[i] < 0:
            negative_left_values -= 1
        if A[i] != 0:
            non_zero_indexes.append(i)

    # manage the cases where A[i] != 0
    for i in range(0, len(non_zero_indexes)):
        count = 0
        for j in range(non_zero_indexes[i] + 1, len(A)):
            if A[j] < A[non_zero_indexes[i]]:
                count += 1
        B[non_zero_indexes[i]] = count

    return B

if __name__ == '__main__':
    A = [2, -7, 8, 3, -5, -5, 9, 1, 12, 4]
    B = exercice2b(A)
    print("B =", B)


    print("----------------------")


    A_zeros = [0, -7, 0, 1, 0, 0, 0, -3, 8, 0]
    B_zeros = exercice2c(A_zeros)
    print("B_zeros = ", B_zeros)




'''
B = [4, 0, 5, 3, 0, 0, 2, 0, 1, 0]
----------------------
B_zeros =  [2, 0, 1, 5, 1, 1, 1, 0, 1, 0]

'''