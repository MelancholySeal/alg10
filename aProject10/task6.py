#!usr/bin/env python3
# -*- coding: utf-8 -*-


def linear_memory_sum(A, B):
    n = len(A)
    A.sort()
    B.sort()
    min_heap = []
    
    min_heap.append((A[0] + B[0], 0, 0))
    result = []

    for _ in range(n * n - 1):
        a_sum, i, j = min_heap.pop(0)
        result.append(a_sum)
        
        if j < n - 1:
            min_heap.append((A[i] + B[j+1], i, j+1))
        if j == 0 and i < n - 1:
            min_heap.append((A[i+1] + B[j], i+1, j))

        min_heap.sort()

    return result


def main():
    A = [3, 1, 2]
    B = [2, 4, 6]
    result = linear_memory_sum(A, B)
    print(result)


if __name__ == "__main__":
    main()