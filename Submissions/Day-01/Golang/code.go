package main

import (
    "bufio"
    "fmt"
    "os"
	"strconv"
	"sort"
)

func elf_calories() []int {
	var elf_calories []int //Defining a slice
	var calories int
	input_file, err := os.Open("input.txt") //Creating a file handle to read the input file

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(input_file) // Creating a filescanner object
	fileScanner.Split(bufio.ScanLines) // Asking the scanner to split the file into lines
	
	for fileScanner.Scan() {
		if fileScanner.Text() == "" {
			calories = 0
		} else {
			intval, err := strconv.Atoi(fileScanner.Text()) // Converting String to int for the numbers

			if err != nil {
				fmt.Println(err)
			}

			calories = calories + intval
			elf_calories=append(elf_calories,calories)
		}
	}
	return elf_calories
}


func main(){
	elf_calories := elf_calories()
	sort.Sort(sort.Reverse(sort.IntSlice(elf_calories))) //Reverse sorting a slice
	fmt.Println(elf_calories[0])
	fmt.Println(elf_calories[0]+elf_calories[1]+elf_calories[2])
}