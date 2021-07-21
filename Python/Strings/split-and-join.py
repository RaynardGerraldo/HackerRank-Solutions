def split_and_join(line):
    # write your code here
    list_line = line.split()
    final_l = '-'.join(list_line)
    return final_l
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
