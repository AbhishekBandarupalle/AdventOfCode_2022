package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
	"strings"
)

func main(){
	var	overlaps int
	var fully_contained_pairs int
	
	inputfile , err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	
	fileScanner := bufio.NewScanner(inputfile)
	fileScanner.Split(bufio.ScanLines)
	for fileScanner.Scan() {
		line := strings.TrimSpace(fileScanner.Text())
		range1 := strings.Split(line,",")[0]
		range2 := strings.Split(line, ",")[1]
		low_range1, err := strconv.Atoi(strings.Split(range1,"-")[0])
		if err != nil {
			fmt.Println(err)
		}
		upper_range1, err := strconv.Atoi(strings.Split(range1,"-")[1])
		if err != nil {
			fmt.Println(err)
		}
		low_range2, err := strconv.Atoi(strings.Split(range2,"-")[0])
		if err != nil {
			fmt.Println(err)
		}
		upper_range2, err := strconv.Atoi(strings.Split(range2,"-")[1])
		if err != nil {
			fmt.Println(err)
		}
		if os.Args[1] == "part1" {
			if low_range1 <= low_range2 && upper_range1 >= upper_range2 {
				fully_contained_pairs+=1
			} else if low_range2 <= low_range1 && upper_range2 >= upper_range1 {
				fully_contained_pairs+=1
			}
		} else if os.Args[1] == "part2" {
			if low_range1 <= low_range2 && upper_range1 <= upper_range2 && upper_range1 >= low_range2{
				overlaps+=1
			} else if low_range2 <= low_range1 && upper_range2 <= upper_range1 && upper_range2 >= low_range1 {
				overlaps+=1
			} else if low_range1 <= low_range2 && upper_range1 >= upper_range2 {
				overlaps+=1
			} else if low_range2 <= low_range1 && upper_range2 >= upper_range1 {
				overlaps+=1
			}
		}
	}
	if os.Args[1] == "part1" {
		fmt.Println(fully_contained_pairs)
	} else if os.Args[1] == "part2" {
		fmt.Println(overlaps)
	}
}