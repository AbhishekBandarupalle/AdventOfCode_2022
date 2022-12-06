package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

/*
This is incomplete. Should read more about slices and maps
*/
var operations []string
var current_stacks = map[string][]string{}

func isNumeric(s string) bool {
	_, err := strconv.ParseFloat(s, 64)
	return err == nil
}

func remove(s []string, r string) []string {
	for i, v := range s {
		if v == r {
			return append(s[:i], s[i+1:]...)
		}
	}
	return s
}

func get_data_from_inputfile() (map[string][]string, []string) {
	regex1 := regexp.MustCompile("^[0-9 ]+$")
	// regex2 := regexp.MustCompile("move")
	inputfile, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	fileScanner := bufio.NewScanner(inputfile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		line := fileScanner.Text()
		if line == "\n" {

		} else {
			line = strings.ReplaceAll(line, "\n", "")
			operations = append(operations, line)
		}
		if regex1.MatchString(line) {
			line = strings.ReplaceAll(line, "\n", "")
			operations = remove(operations, line)
			tmplist2 := strings.Split(line, " ")
			for i := 0; i < len(tmplist2); i++ {
				if isNumeric(tmplist2[i]) {
					current_stacks[tmplist2[i]] = nil
				}
			}
		}
	}
	fmt.Println(operations)
	return current_stacks, operations
}

func main() {
	current_stacks, operations := get_data_from_inputfile()
	fmt.Println(current_stacks)
	fmt.Println(operations)
}
