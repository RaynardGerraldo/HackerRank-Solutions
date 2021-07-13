def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        elif i == 0:
            zero += 1
    
    res_pos = pos / len(arr)
    neg_pos = neg / len(arr)
    zero_pos = zero / len(arr)
    
    final = format(res_pos, '.6f'),format(neg_pos, '.6f'),format(zero_pos, '.6f')
    return "\n".join(final)

# Hacker rank format answer
#if __name__ == '__main__':
    #n = int(input().strip())

    #arr = list(map(int, input().rstrip().split()))

    #print(plusMinus(arr))

