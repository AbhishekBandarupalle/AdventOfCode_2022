import sys

def part1(opponent,me,winning_rounds,played_score,round_score):
    xyz_convert={'X': 'rock', 'Y': 'paper', 'Z': 'scissors'} 
    if xyz_convert[me] == winning_rounds[opponent]:
        my_score=played_score[xyz_convert[me]]+round_score['win']
    elif xyz_convert[me]==opponent:
        my_score=played_score[xyz_convert[me]]+round_score['draw']
    else:
        my_score=played_score[xyz_convert[me]]
    return my_score

def part2(opponent,me,winning_rounds,played_score,round_score):
    xyz_convert={'X': 'lose', 'Y': 'draw', 'Z': 'win'}
    losing_rounds=dict((v,k) for (k,v) in winning_rounds.items())
    if xyz_convert[me] == 'win':
        my_score=played_score[winning_rounds[opponent]]+round_score['win']
    elif xyz_convert[me] == 'draw':
        my_score=played_score[opponent]+round_score['draw']
    else:
        my_score=played_score[losing_rounds[opponent]]
    return my_score

def main():
    played_score={'rock': 1, 'paper': 2, 'scissors': 3}
    round_score={'win': 6, 'draw': 3}
    winning_rounds={'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'} #Opponent hand is key and my hand is value
    abc_convert={'A': 'rock', 'B': 'paper', 'C': 'scissors'} 
    my_final_score=0
    with open('input.txt','r') as strategy:
        for line in strategy.readlines():
            opponent,me=line.strip().split(' ')
            opponent=abc_convert[opponent]
            if sys.argv[1]=='part1':
                my_final_score+=part1(opponent,me,winning_rounds,played_score,round_score)
            elif sys.argv[1]=='part2':
                my_final_score+=part2(opponent,me,winning_rounds,played_score,round_score)
    strategy.close()
    print(my_final_score)

if __name__=="__main__":
    main()