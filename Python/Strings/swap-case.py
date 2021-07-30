def swap_case(s):
    s_list = []
    for i in s:
        if i == i.lower():
           s_list.append(i.upper())
        else:
           s_list.append(i.lower())
            
    return ''.join(s_list)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
