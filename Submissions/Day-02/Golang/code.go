package main

import (
    "bufio"
    "fmt"
    "os"
	"strings"
)
/*
This code is Golang equivalent of the Python Code
*/

var round_score = map[string]int {"win": 6, "draw": 3}
var played_score = map[string]int {"rock": 1, "paper": 2, "scissors": 3}
var winning_rounds = map[string]string {"rock": "paper", "paper": "scissors", "scissors": "rock"} // #Opponent hand is key and my hand is value
var abc_convert = map[string]string {"A": "rock", "B": "paper", "C": "scissors"} 
var my_score int
var opponent string
var me string

func main(){
	my_final_score := 0
	strategy, err := os.Open("input.txt")
	if err!= nil {
		fmt.Println(err)
	}
	fileScanner := bufio.NewScanner(strategy)
	fileScanner.Split(bufio.ScanLines)
	for fileScanner.Scan(){
		line:=strings.TrimSpace(fileScanner.Text())
		opponent := strings.Split(line, " ")[0]
		me := strings.Split(line, " ")[1]
		opponent = abc_convert[opponent]
		if os.Args[1] == "part1"{
			my_final_score+=part1(opponent,me,round_score,winning_rounds,played_score)
		}
		if os.Args[1] == "part2"{
			my_final_score+=part2(opponent,me,round_score,winning_rounds,played_score)
		}
	}
	fmt.Println(my_final_score)
}

func part1(opponent string, me string, round_score map[string]int, winning_rounds map[string]string, played_score map[string]int) int {
	xyz_convert := map[string]string {"X": "rock", "Y": "paper", "Z": "scissors"} 
	//fmt.Println(opponent, " ", xyz_convert[me])
	if xyz_convert[me] == winning_rounds[opponent] {
		my_score = played_score[xyz_convert[me]] + round_score["win"]
	} else if xyz_convert[me] == opponent {
		my_score = played_score[xyz_convert[me]] + round_score["draw"]
	} else {
		my_score = played_score[xyz_convert[me]]
	}
	//fmt.Println(my_score)
	return my_score
}

func part2(opponent string, me string, round_score map[string]int, winning_rounds map[string]string, played_score map[string]int) int {
	xyz_convert := map[string]string {"X": "lose", "Y": "draw", "Z": "win"}
	if xyz_convert[me] == "win" {
		my_score = played_score[winning_rounds[opponent]]+round_score["win"]
	} else if xyz_convert[me] == "draw" {
		my_score = played_score[opponent]+round_score["draw"]
	} else {
		my_score = 6 - played_score[opponent] - played_score[winning_rounds[opponent]]
	}
	return my_score
}