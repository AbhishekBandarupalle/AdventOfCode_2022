import day_01

def part1(elf_calories): 
    return max(elf_calories)

def part2(elf_calories):
    elf_calories.sort(reverse=True)
    return (elf_calories[0] + elf_calories[1] + elf_calories[2])

def main():
    elfcalories=day_01.elf_calories(inputfile="input.txt")
    answer1 = part1(elf_calories=elfcalories)
    answer2 = part2(elf_calories=elfcalories)
    print(answer1)
    print(answer2)
    
if __name__=="__main__":
    main()
