package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
)

/* 
Note to self: Using for loops for finding common characters between strings is inefficient, should find a better way to do it in go.
*/

func get_priority(item byte) int {
	var priority int
	ascii:= int(item)
	if ascii >= 97 {
		priority = (ascii - 96)
	} else if ascii < 97 {
		priority = (ascii - 38)
	}
	return priority
}

func main(){
	var final_priority int
	var group []string
	var common_char byte
	inputfile, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(nil)
	}
	fileScanner := bufio.NewScanner(inputfile)
	fileScanner.Split(bufio.ScanLines)
	for fileScanner.Scan(){
		line := strings.TrimSpace(fileScanner.Text())
		if os.Args[1] == "part1" {
			compartment1 := line[:len(line)/2]
			compartment2 := line[len(line)/2:]
			for i:=0 ; i<len(compartment1); i++ {
				for j:=0; j<len(compartment2); j++ {
					if compartment1[i] == compartment2 [j] {
						common_char = compartment1[i]
					}
				}
			}
			final_priority += get_priority(common_char)
		} else if os.Args[1] == "part2" {
			if len(group) == 2 {
				group=append(group,line)
				for i:=0; i<len(group[0]); i++ {
					for j:=0; j<len(group[1]); j++ {
						for k:=0; k<len(group[2]); k++ {
							if group[0][i] == group[1][j] {
								if group[0][i] == group[2][k] {
									common_char = group[0][i]
								}
							}   
						}
					}
				}
				group = nil
				final_priority += get_priority(common_char)
			} else {
				group=append(group,line)
			}
				
			}

		}
	fmt.Println(final_priority)
}