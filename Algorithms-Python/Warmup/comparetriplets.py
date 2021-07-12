def compareTriplets(a, b):
    res_arr = [0,0]
    # Write your code here
    for i,j in zip(a,b):
        if i < j:
            res_arr[1] = res_arr[1] + 1
        if i > j:
            res_arr[0] = res_arr[0] + 1
        if i == j:
            pass

    return res_arr

a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)

print(result)

# Hacker rank answer format
# if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #a = list(map(int, input().rstrip().split()))

    #b = list(map(int, input().rstrip().split()))

    #result = compareTriplets(a, b)
 
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
