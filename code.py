def standard():
    A = [2, -7, 8, 3, -5, -5, 9, 1, 12, 4]
    B = [0 for i in range(0, len(A))]
    for i in range(0, len(A)):
        cout = 0
        for j in range(i+1, len(A)):
            if A[j] < A[i]:
                cout += 1
        B[i] = cout
    print(A)
    print(B)

def zero_version():
    A = [0, -7, 0, 1, 0, 0, 0, -3, 8, 0]
    B = [-1 for i in range(0, len(A))]
    index_non_zero = []


    negative_left_values = 0
    # count negative_left_values
    for i in range(0, len(A)):
        if A[i] < 0:
            negative_left_values += 1

    # manage all the case where A[i] = 0
    for i in range(0, len(A)):
        if A[i] == 0:
            B[i] = negative_left_values
        if A[i] < 0:
            negative_left_values -= 1
        if A[i] != 0:
            index_non_zero.append(i)

    # loop for a constant time
    for i in range(0, len(index_non_zero)):
        cout = 0
        for j in range(index_non_zero[i] + 1, len(A)):
            if A[j] < A[index_non_zero[i]]:
                cout += 1
        B[index_non_zero[i]] = cout

    print(A)
    print(B)

if __name__ == '__main__':
    zero_version()


