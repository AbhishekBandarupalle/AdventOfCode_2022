import sys

def four_non_repeating_chars(inputdata):
    '''
    Returns start of packet marker
    '''
    start_index=0
    while start_index < len(inputdata)-4:
        if len(set(inputdata[start_index:start_index+4])) == 4:
            return start_index+4
        else: 
            start_index+=1

def fourteen_distinct_chars(inputdata):
    '''
    Returns start of message marker
    '''
    start_index=0
    while start_index < len(inputdata)-14:
        if len(set(inputdata[start_index:start_index+14])) == 14:
            return start_index+14
        else: 
            start_index+=1


def main():
    try:
        with open(sys.argv[1],'r') as inputbuffer:
            inputstring=inputbuffer.read()
    except FileNotFoundError as e:
        print("File Not found: {}".format(e))
    if len(sys.argv) == 2 and sys.argv[2] == "part1":
        start_of_packet_marker = four_non_repeating_chars(inputdata=inputstring)
        print(start_of_packet_marker)
    elif len(sys.argv) == 2 and sys.argv[2] == "part2":
        start_of_message_marker = fourteen_distinct_chars(inputdata=inputstring)
        print(start_of_message_marker)
    elif len(sys.argv) > 2 and sys.argv[2] == "part1" and sys.argv[3] == "part2":
        start_of_packet_marker = four_non_repeating_chars(inputdata=inputstring)
        print("Start of Packet Marker: {}".format(start_of_packet_marker))
        start_of_message_marker = fourteen_distinct_chars(inputdata=inputstring)
        print("Start of Message Marker: {}".format(start_of_message_marker))


if __name__=="__main__":
    main()