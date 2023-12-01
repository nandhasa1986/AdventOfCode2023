import re

inputfp = open('input.txt', 'r')
totalcalib = 0

numbers = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]

while True:
    s1 = inputfp.readline().strip()
    if not s1:
        break

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
