def miniMaxSum(arr):
    arr.sort()
    min_sort = arr[:-1]
    max_sort = arr[1:5]
    res = sum(min_sort)
    res2 = sum(max_sort)
    
    print(res, end= " "),print(res2)

#Hacker rank answer format(remove comments to use) 
#if __name__ == '__main__':  

    #arr = list(map(int, input().rstrip().split()))

    #miniMaxSum(arr)

