if __name__ == '__main__':
    X = int(input())
    Y = int(input())
    Z = int(input())
    N = int(input())
    
res = [[x,y,z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if sum([x,y,z]) != N]            

print(res)



