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
    
        if line[markindex] not in non_symbols:
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
        if line[index] not in non_symbols:
            return True 
        else:
            return False

    if index == linelen:
        if line[index - numlen - 1] not in non_symbols:
            return True 
        else:
            return False

    if line[index - numlen - 1] not in non_symbols or line[index] not in non_symbols:
        return True

    return False

selected_numbers = []
prev = []
start = True
while True:
    if start:
        curr = inputfp.readline().strip()
        start = False
        prev = []
        next = inputfp.readline().strip()
    else:
        prev = curr
        curr = next
        next = inputfp.readline().strip() 


    index = 0
    numfind = ""
    while index < len(curr):
        if curr[index] in numbers:
            numfind += curr[index]
        else:
            if numfind:
                if check_valid_number(prev, numfind, index) or check_valid_number(next, numfind, index) or check_valid_curr_line_number(curr, numfind, index):
                    print("Selected Number " + str(numfind))
                    print("prev " + str(check_valid_number(prev, numfind, index)))
                    print("next " + str(check_valid_number(next, numfind, index)))
                    print("curr " + str(check_valid_curr_line_number(curr, numfind, index)))
                    selected_numbers.append(numfind)
            numfind = ""
        index += 1
    if numfind:
        if check_valid_number(prev, numfind, index) or check_valid_number(next, numfind, index) or check_valid_curr_line_number(curr, numfind, index):
            selected_numbers.append(numfind)

    if not next:
        # check on previous line case   
        break

inputfp.close()

print(selected_numbers)

total = 0
for numbers in selected_numbers:
     total += int(numbers)

print(str(total))
