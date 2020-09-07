def solution(arr1, arr2):
    return [[a+b for a, b in zip(arr1[i], arr2[i])] for i in range(len(arr1))]