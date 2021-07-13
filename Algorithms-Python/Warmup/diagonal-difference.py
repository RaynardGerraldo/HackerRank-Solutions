def diagonalDifference(arr):
    first_diag, sec_diag = 0,0
    for i in range(len(arr)):
        first_diag += arr[i][i]
        sec_diag += arr[len(arr)-i-1][i]
    return abs(first_diag - sec_diag)

# Hacker rank format answer(Remove comments to make it work on hacker rank)
#if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input().strip())

    #arr = []

    #for _ in range(n):
        #arr.append(list(map(int, input().rstrip().split())))

    #result = diagonalDifference(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()

