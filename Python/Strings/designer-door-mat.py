# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

lw = input().split()

width = int(lw[0])
length = int(lw[1])

def reverse_design(width,length,count):
    for l in reversed(range(count)):
        times = l * 2 + 1
        final_pattern = ".|." * times
        count_pattern = math.ceil((length - len(final_pattern)) // 2)
        print("{}{}{}".format("-" * count_pattern, final_pattern, "-" * count_pattern))
            
        
def designer(width,length):
    for l in range(width):
        times = l * 2 + 1
        final_pattern = ".|." * times
        count_pattern = math.ceil((length - len(final_pattern)) // 2)
        welcome_pattern = int(math.ceil(width / 2)) - 1
        
        if l == welcome_pattern:
            welcome_count = (length - len("WELCOME")) // 2
            print("{}{}{}".format("-" * welcome_count, "WELCOME", "-" * welcome_count))
            reverse_design(width,length,l)
            break
                                 
        print("{}{}{}".format("-" * count_pattern, final_pattern, "-" * count_pattern))
                         

designer(width,length)        

