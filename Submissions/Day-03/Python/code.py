import sys
        
def get_priority(common_char):
    if common_char.islower():
        priority = ord(common_char)-96
    elif common_char.isupper():
        priority = ord(common_char)-38
    return priority

def main():
    priority=0
    group=[]
    with open("input.txt", 'r') as inputfile:
        for line in inputfile.readlines():
            line = line.strip()      
            if sys.argv[1] == "part1":
                compartment1=line[:len(line)//2]
                compartment2=line[len(line)//2:]   
                for char in compartment1:
                    if char in compartment2:
                        common_char=char
                priority += get_priority(common_char=common_char)
            if sys.argv[1] == "part2":
                if len(group)==2:
                        group.append(line)
                        for char in group[0]:
                            if char in group[1] and char in group[2]:
                                common_char=char
                        group=[]
                        priority += get_priority(common_char=common_char)
                else:
                    group.append(line)
    inputfile.close()
    print(priority)

if __name__=="__main__":
    main()