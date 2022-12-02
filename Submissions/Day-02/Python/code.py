import sys

def part1(opponent,me,played_score,round_score):
    if opponent=='A':
        if me == 'X':
            my_score=played_score['rock']+round_score['draw']
        elif me == 'Y':
            my_score=played_score['paper']+round_score['win']
        elif me == 'Z':
            my_score=played_score['scissors']+round_score['lose']
    elif opponent=='B':
        if me == 'X':
            my_score=played_score['rock']+round_score['lose']
        elif me == 'Y':
            my_score=played_score['paper']+round_score['draw']
        elif me == 'Z':
            my_score=played_score['scissors']+round_score['win']
    elif opponent=='C':
        if me == 'X':
            my_score=played_score['rock']+round_score['win']
        elif me == 'Y':
            my_score=played_score['paper']+round_score['lose']
        elif me == 'Z':
            my_score=played_score['scissors']+round_score['draw']
    return my_score

def part2(opponent,me,played_score,round_score):
    if opponent=='A':
        if me == 'X':
            my_score=played_score['scissors']+round_score['lose']
        elif me == 'Y':
            my_score=played_score['rock']+round_score['draw']
        elif me == 'Z':
            my_score=played_score['paper']+round_score['win']
    elif opponent=='B':
        if me == 'X':
            my_score=played_score['rock']+round_score['lose']
        elif me == 'Y':
            my_score=played_score['paper']+round_score['draw']
        elif me == 'Z':
            my_score=played_score['scissors']+round_score['win']
    elif opponent=='C':
        if me == 'X':
            my_score=played_score['paper']+round_score['lose']
        elif me == 'Y':
            my_score=played_score['scissors']+round_score['draw']
        elif me == 'Z':
            my_score=played_score['rock']+round_score['win']
    return my_score

def main():
    played_score={'rock': 1, 'paper': 2, 'scissors': 3}
    round_score={'win': 6, 'draw': 3, 'lose': 0}
    my_final_score=0
    with open('input.txt','r') as strategy:
        for line in strategy.readlines():
            opponent,me=line.strip().split(' ')
            if sys.argv[1]=='part1':
                my_final_score+=part1(opponent,me,played_score,round_score)
            elif sys.argv[1]=='part2':
                my_final_score+=part2(opponent,me,played_score,round_score)
    print(my_final_score)

if __name__=="__main__":
    main()