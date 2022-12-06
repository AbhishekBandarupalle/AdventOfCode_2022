import sys
import re

def get_data_into_dict():
    crates=[]
    operations = []
    stacks_crates = {}
    try:
        listvar=crates
        with open(sys.argv[1],'r') as inputfile: 
            for line in inputfile.readlines():
                if line == "\n":
                    listvar=operations
                else:
                    line=line.replace("\n","")
                    listvar.append(line)

                if re.findall("^[0-9 ]+$",line):
                    line=line.replace("\n","")
                    listvar.remove(line)
                    for i in line.split(" "):
                        if i.isnumeric():
                            stacks_crates[i]=stacks_crates.get(i,[]) # Get stacks which are the keys to dictionary
        inputfile.close()

        for line in crates: # Get crates in each stack - values for the keys
            i=0
            for key in stacks_crates.keys():
                if line[1+i]!=" ":
                    stacks_crates[key].append(line[1+i])
                if i<len(line)-6:
                    i+=4
        return stacks_crates,operations

    except FileNotFoundError as e:
        print("File Not found: {}".format(e))


def move_stacks_part1():
    stacks_crates,operations = get_data_into_dict()
    source=""
    destination=""
    num_of_stacks=0
    moving_stack=""
    for line in operations:
        num_of_stacks,source,destination = re.findall("\d+",line)
        num_of_stacks = int(num_of_stacks)
        for i in range(num_of_stacks):
            moving_stack=stacks_crates[source][0]
            stacks_crates[source].remove(moving_stack)
            stacks_crates[destination].insert(0,moving_stack)
    return stacks_crates

def move_stacks_part2():
    current_stack,operations=get_data_into_dict()
    source=""
    destination=""
    num_of_stacks=0
    moving_stack=""
    for line in operations:
        num_of_stacks,source,destination = re.findall("\d+",line)
        num_of_stacks = int(num_of_stacks)
        for i in range(num_of_stacks):
            moving_stack=current_stack[source][0]
            current_stack[source].remove(moving_stack)
            current_stack[destination].insert(i,moving_stack)
    return current_stack

def get_top_stack(updated_stack_data):
    final_result=""
    for key in updated_stack_data:
        final_result+=updated_stack_data[key][0]
    return final_result

def main():
    if sys.argv[2] == "part1":
        moved_stacks = move_stacks_part1()
        answer = get_top_stack(updated_stack_data=moved_stacks)
        print(answer)
    if sys.argv[2] == "part2":
        moved_stacks = move_stacks_part2()
        answer = get_top_stack(updated_stack_data=moved_stacks)
        print(answer)

if __name__=="__main__":
    main()