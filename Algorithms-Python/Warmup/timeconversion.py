def timeConversion(s):
    l_s = []
    if "PM" in s:
        if "PM" in s and "12" in s:
            s = s.replace('PM','')
            return s
        s = s.replace('PM','')
        list_s = [i for i in s]
        to_replace = list_s[0],list_s[1]
        s = s.replace(''.join(to_replace), str(int(''.join(to_replace))+12))
        return s
        
    elif "AM" in s:
        if "AM" in s and "12" in s:
            s = s.replace('AM','')
            s = s.replace("12", "00")
            return s
        s = s.replace('AM', '')
        return s

#Hacker rank answering format(remove comments to use)    
#if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = input()

    #result = timeConversion(s)

    #fptr.write(result + '\n')

    #fptr.close()
