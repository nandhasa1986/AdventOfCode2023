import re

inputfp = open('input.txt', 'r')
totalcalib = 0

numbers = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]

while True:
    s1 = inputfp.readline().strip()
    if not s1:
        break
    s1index = 0
    while s1index < len(s1):
        matchFound = False
        for index in range(0, len(numbers)):
            #print("Start " + s1 + " " + str(s1index) + " " + str(index) + " " + str(len(numbers[index])) + " " + s1[s1index:][:len(numbers[index])])
            if s1[s1index:][:len(numbers[index])] == numbers[index]:
                #print("Matched " + " " + s1[:s1index] + " " + str(index + 1) + " " + s1[s1index + 1:])
                s1 = s1[:s1index] + str(index + 1) + s1[s1index:]
                s1index += len(numbers[index]) - 1
                matchFound = True
                #print(s1index)
                break
        if not matchFound:
            s1index += 1

    m = re.search(r"\d.*\d", s1)
    calibvalue = 0
    if m == None:
        m = re.search(r"\d", s1)
        calibvalue = int(s1[m.start()] + s1[m.start()])
    else:
        calibvalue = int(s1[m.start()] + s1[m.end() - 1])

    if calibvalue != 0:
        totalcalib += calibvalue

    print(s1 + " " + str(calibvalue))
    #print(s1[m.start()] + " " + s1[m.end() - 1])

print(totalcalib)
inputfp.close()
