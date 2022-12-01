"""
    Module to contain all common functions for Day-01 of AoC-2022
"""    
def elf_calories(inputfile): 
    '''
        Read the input file and create a list of intergers for calories of each elf as a single entry in the list
    '''
    elf_calories=[]
    with open(inputfile,'r') as input_data:
        calories=0
        for line in input_data.readlines(): 
            line=line.strip()
            if line=="":
                calories=0
            else:
                calories+=int(line)
                elf_calories.append(calories)
    return elf_calories
