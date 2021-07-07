#! /usr/bin/env python3
def runnerup(n,arr):
    arr_sorted = sorted(arr)
    arr_sorted = list(dict.fromkeys(arr_sorted))
    print(arr_sorted[-2])
runnerup(int(input()), map(int, input().split()))



