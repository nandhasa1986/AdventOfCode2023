import re

inputfp = open('input.txt', 'r')

symbols = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '#', '$' ]
numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
non_symbols = [ '.' ]

def check_valid_number(line, numfind, index):
    numlen = len(numfind)
    linelen = len(line)
    numcheck = False

    if not line:
        return False

    indexprev = 0
    while indexprev < (numlen + 2):
        markindex = index + indexprev - numlen - 1
        print(str(numfind) + " " + str(markindex) + " " + str(numlen) + " " + str(linelen) + " " + str(index) + " " + str(indexprev))

        if markindex < 0:
            pass

        if markindex >= linelen:
            break
    
        #if line[markindex] not in non_symbols:
        if line[markindex] in '*':
            numcheck = True
            break
        indexprev += 1
    return numcheck 

def check_valid_curr_line_number(line, numfind, index):
    numlen = len(numfind)
    linelen = len(line)
    markindex = index - numlen
    numcheck = False

    if index - numlen <= 0:
        if line[index] in '*':
            return True 
        else:
            return False

    if index == linelen:
        if line[index - numlen - 1] in '*':
            return True 
        else:
            return False

    if line[index - numlen - 1] in '*' or line[index] in '*':
        return True

    return False

def find_numbers_before_after(lines, index):
    line_len = len(lines)
    left = right = index 
    if index > line_len - 1 or index < 0:
        return ""
    if lines[index] in numbers:
        inc = 1
        if (index + inc) < line_len:
            while lines[index + inc] in numbers:
                inc += 1
        right = index + inc
        dec = 1
        if (index - dec) > 0:
            while lines[index - dec] in numbers:
                dec += 1
            left = index - dec + 1
        #print("Left " + str(left) + " Right " + str(right))
        return str(lines[left:right])
    return ""

class Gear:
    def __init__(self, top, bottom):
        self.top = int(top)
        self.bottom = int(bottom)
        self.value = self.top * self.bottom

def find_curr_line_num_left_index(lines, indexWL):
    numfindC = find_numbers_before_after(lines, indexWL - 1)
    return numfindC

def find_curr_line_num_right_index(lines, indexWL):
    numfindC = find_numbers_before_after(lines, indexWL + 1)
    return numfindC
  
def find_TB_line_num_index(lines, indexWL):
    numfindL = numfindR = ""
    numfind = find_numbers_before_after(lines, indexWL)
    if not numfind:
        numfindL = find_numbers_before_after(lines, indexWL - 1)
    if not numfind:
        numfindR = find_numbers_before_after(lines, indexWL + 1)
    return [numfind, numfindL, numfindR]

selected_numbers = []
selected_gears = []
prev = []
start = True
index = 0
lines = []

# Open the file in read mode
with open('input.txt', 'r') as file:
    # Create an empty list to store the lines

    # Iterate over the lines of the file
    for line in file:
        # Remove the newline character at the end of the line
        line = line

        # Append the line to the list
        lines.append(line)
        index += 1

max_lines = index

indexL = 0
while indexL < max_lines:
    indexWL = 0
    while indexWL < len(lines[indexL]):
        numfindT = "" # Top
        numfindTL = "" # Top
        numfindTR = "" # Top
        numfindL = "" # Current Left
        numfindR = "" # Current Right
        numfindB = "" # Middle
        numfindBL = "" # Middle
        numfindBR = "" # Middle
        top = bottom = None
        if lines[indexL][indexWL] in '*':
            #print("Found * at index " + str(indexL) + " " + str(indexWL))
            if indexL == 0:
                # Look in Same Line
                numfindL = find_curr_line_num_left_index(lines[indexL], indexWL)
                numfindR = find_curr_line_num_right_index(lines[indexL], indexWL)

                # Look at Bottom Line
                [numfindB, numfindBL, numfindBR] = find_TB_line_num_index(lines[indexL + 1], indexWL)
            elif indexL == max_lines - 1:
                # Look in Same Line
                numfindL = find_curr_line_num_left_index(lines[indexL], indexWL)
                numfindR = find_curr_line_num_right_index(lines[indexL], indexWL)

                # Look for Top Line
                [numfindT, numfindTL, numfindTR] = find_TB_line_num_index(lines[indexL - 1], indexWL)
            else:
                # Look for Top Line
                [numfindT, numfindTL, numfindTR] = find_TB_line_num_index(lines[indexL - 1], indexWL)

                # Look in Same Line
                numfindL = find_curr_line_num_left_index(lines[indexL], indexWL)
                numfindR = find_curr_line_num_right_index(lines[indexL], indexWL)

                # Look at Bottom Line
                [numfindB, numfindBL, numfindBR] = find_TB_line_num_index(lines[indexL + 1], indexWL)
            print("numfind " + str(numfindT) + " " + str(numfindL) + " " + str(numfindR) + " " + str(numfindB))
            if numfindT:
               top = numfindT
               bottom =       "" + numfindB + numfindL + numfindR + numfindBL + numfindBR + numfindTL + numfindTR
            elif numfindL:
               top = numfindL
               bottom = numfindT + numfindB + ""       + numfindR + numfindBL + numfindBR + numfindTL + numfindTR
            elif numfindR:
               top = numfindR
               bottom = numfindT + numfindB + numfindL + ""       + numfindBL + numfindBR + numfindTL + numfindTR
            elif numfindB:
               top = numfindB
               bottom = numfindT + ""       + numfindL + numfindR + numfindBL + numfindBR + numfindTL + numfindTR
            elif numfindTL:
               top = numfindTL
               bottom = numfindT + numfindB + numfindL + numfindR + numfindBL + numfindBR + ""        + numfindTR
            elif numfindTR:
               top = numfindTR
               bottom = numfindT + numfindB + numfindL + numfindR + numfindBL + numfindBR + numfindTL + ""
            elif numfindBL:
               top = numfindBL
               bottom = numfindT + numfindB + numfindL + numfindR + ""        + numfindBR + numfindTL + numfindTR
            elif numfindBR:
               top = numfindBR
               bottom = numfindT + numfindB + numfindL + numfindR + numfindBL + ""        + numfindTL + numfindTR
            #if not numfindT:
            #    top = numfindL
            #    bottom = numfindB
            #if not numfindB:
            #    top = numfindT
            #    bottom = numfindR
            #if not numfindL:
            #    top = numfindT
            #    bottom = numfindB
            print("Top " + str(top) + " " + str(bottom))
            if top and bottom:
                gear = Gear(top, bottom)
                selected_gears.append(gear)
        #print("Line " + str(indexL) + " " + str(indexWL))
        indexWL += 1
    indexL += 1 


inputfp.close()

total = 0
for numbers1 in selected_gears:
     print(str(numbers1.top) + " " + str(numbers1.bottom) + " " + str(numbers1.value))
     total += int(numbers1.value)

print(str(total))
