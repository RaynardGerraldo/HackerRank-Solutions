def gradingStudents(grades):
    final_res = []
    for i in grades:
        div_5 = i // 5
        mult_5 = (div_5 + 1) * 5
        res_min = mult_5 - i
        if i == 40:
            final_res.append(i)
        elif i < 38:
            final_res.append(i)
        elif i < 40:
            if res_min < 3:
                final_res.append(mult_5)
            elif res_min >= 3:
                final_res.append(i)
        elif i > 40:
            if res_min < 3:
                final_res.append(mult_5)
            elif res_min >= 3:
                final_res.append(i)
    
    return final_res

#Hackerrank answer format(remove comments to use)
#if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #grades_count = int(input().strip())

    #grades = []

    #for _ in range(grades_count):
        #grades_item = int(input().strip())
        #grades.append(grades_item)

    #result = gradingStudents(grades)

    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
