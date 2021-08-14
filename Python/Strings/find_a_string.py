def count_substring(string, sub_string):
    cou = 0
    for i in range(len(string)):
        if string.startswith(sub_string, i):
            cou += 1
    return cou

#Hacker Rank answering format(remove to run)
#if __name__ == '__main__':
    #string = input().strip()
    #sub_string = input().strip() 
    #count = count_substring(string, sub_string)
    #print(count)
