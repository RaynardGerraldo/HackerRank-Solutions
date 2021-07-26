def mutate_string(string, position, character):
    mutate = [i for i in string]
    mutate[position] = character
    return ''.join(mutate)

# Hacker rank answering format(remove comments to use)
#if __name__ == '__main__':
    #s = input()
    #i, c = input().split()
    #s_new = mutate_string(s, int(i), c)
    #print(s_new)
