import sys

def main():
    fully_contained_pairs=0
    overlaps=0
    try:
        with open("input.txt", "r") as inputfile:
            for line in inputfile.readlines():
                line=line.strip()
                range1,range2=line.split(",")
                low_range1,upper_range1=int(range1.split("-")[0]),int(range1.split("-")[1])
                low_range2,upper_range2=int(range2.split("-")[0]),int(range2.split("-")[1])
                if sys.argv[1] == "part1":
                    if low_range1 <= low_range2 and upper_range1 >= upper_range2: 
                        fully_contained_pairs+=1
                    elif low_range2 <= low_range1 and upper_range2 >= upper_range1:
                        fully_contained_pairs+=1
                elif sys.argv[1] == "part2":
                    if low_range1 <= low_range2 and upper_range1 <= upper_range2 and upper_range1 >= low_range2:
                        #print("{}-{},{}-{}".format(low_range1,upper_range1,low_range2,upper_range2))
                        overlaps+=1
                    elif low_range2 <= low_range1 and upper_range2 <= upper_range1 and upper_range2 >= low_range1:
                        #print("{}-{},{}-{}".format(low_range1,upper_range1,low_range2,upper_range2))
                        overlaps+=1
                    elif low_range1 <= low_range2 and upper_range1 >= upper_range2: 
                        #print("{}-{},{}-{}".format(low_range1,upper_range1,low_range2,upper_range2))
                        overlaps+=1
                    elif low_range2 <= low_range1 and upper_range2 >= upper_range1:
                        #print("{}-{},{}-{}".format(low_range1,upper_range1,low_range2,upper_range2))
                        overlaps+=1
        inputfile.close()
    except FileNotFoundError as e:
        print("File not found. {}".format(e))
    
    if sys.argv[1] == "part1":
        print(fully_contained_pairs)
    elif sys.argv[1] == "part2": 
        print(overlaps) 

if __name__=="__main__":
    main()