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
    indexes_of_non_zero = []
    negative_right_values = 0

    # manage all the cases where A[i] = 0
    for i in range(len(A)-1, -1, -1):
        if A[i] == 0:
            B[i] = negative_right_values
        if A[i] < 0:
            negative_right_values += 1
        if A[i] != 0:
            indexes_of_non_zero.append(i)

    # manage the cases where A[i] != 0
    while len(indexes_of_non_zero) > 0:
        count = 0
        index = indexes_of_non_zero.pop()
        for j in range(index + 1, len(A)):
            if A[j] < A[index]:
                count += 1
        B[index] = count

    return B


def is_first_pair_minor(tuple1, tuple2):
    if(tuple1[0] != tuple2[0]):
        return tuple1[0] < tuple2[0]
    else:
        return tuple1[1] <= tuple2[1]


def mergeSort(array):
    if len(array) > 1:

        arr = array

        # Finding the mid of the array
        mid = len(array) // 2
        L = [0]*mid
        R = [0]*(len(arr)-mid)
        for i in range(0, len(arr)):
            if(i<mid):
                L[i] = arr[i]
            else:
                R[i-mid] = arr[i]


        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if is_first_pair_minor(L[i], R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


if __name__ == '__main__':
    #'''
    A = [2, -7, 8, 3, -5, -5, 9, 1, 12, 4]
    B = exercice2b(A)
    print("B =", B)
    #'''

    '''
    C = [(5, 2), (5, 1), (9, 1), (1, 4), (5, 1), (-7, 8),(2, 19), (9, 1)]
    mergeSort(C)
    print(C)
    '''

