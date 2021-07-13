def staircase(n):
    # Write your code here
    hash = ""
    for i in range(n):
        hash += "#"
        print(hash.rjust(n).format("\n"))

#Hacker Rank answer format(remove comments to use)
#if __name__ == '__main__':
   #n = int(input().strip())

    #staircase(n)
