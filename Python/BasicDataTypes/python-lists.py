if __name__ == '__main__':
    N = int(input())
    list_ = []
    for i in range(N):
        cmd = input()
        li_cmd = list(cmd.split(" "))
        if len(li_cmd) == 3:
            if li_cmd[0] == 'insert':
                list_.insert(int(li_cmd[1]),int(li_cmd[2]))
        
        elif len(li_cmd) == 2:
            if li_cmd[0] == 'append':
                list_.append(int(li_cmd[1]))
            elif li_cmd[0] == 'remove':
                list_.remove(int(li_cmd[1]))
        
        elif len(li_cmd) == 1:
            if li_cmd[0] == 'sort':
                list_.sort()
            elif li_cmd[0] == 'pop':
                list_.pop()
            elif li_cmd[0] == 'reverse':
                list_.reverse()
            elif li_cmd[0] == 'print':
                print(list_)
                
        elif len(li_cmd) == 0:
            if li_cmd[0] == 'print':
                print(list_)
