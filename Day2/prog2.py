import re

inputfp = open('input.txt', 'r')

class SetsRGBValues:
    def __init__(self, R, G, B):
        self.R = int(R)
        self.G = int(G)
        self.B = int(B)

class Games:
    def __init__(self, id, sets):
        self.id = id
        self.sets = sets
        self.maxRGBvalues = SetsRGBValues(0, 0, 0)

gamesList = []
while True:
    s1 = inputfp.readline().strip()
    if not s1:
        break
    lines = s1.split(":")
    id = lines[0].split(" ")[1]
    RGBsets = lines[1].split(";")
    sets = []
    maxRGBvalues = SetsRGBValues(0, 0, 0)
    for RGBset in RGBsets:
        RGBset = RGBset.strip()
        RorGorB = re.split(", | ", RGBset)
        index = R = G = B = 0
        print(RorGorB)
        while index < len(RorGorB):
            if RorGorB[index + 1] == "red":
                R = RorGorB[index]
            elif RorGorB[index + 1] == "green":
                G = RorGorB[index]
            elif RorGorB[index + 1] == "blue":
                B = RorGorB[index]
            index += 2 
        setsRGBValue = SetsRGBValues(R, G, B)
        sets.append(setsRGBValue)
    games = Games(id, sets)

    for maxRGB in sets:
        if maxRGB.R > games.maxRGBvalues.R:
            games.maxRGBvalues.R = maxRGB.R
        if maxRGB.G > games.maxRGBvalues.G:
            games.maxRGBvalues.G = maxRGB.G
        if maxRGB.B > games.maxRGBvalues.B:
            games.maxRGBvalues.B = maxRGB.B
    gamesList.append(games)

inputfp.close()

for games in gamesList:
    print(str(games.id), end = " ")
    for sets in games.sets:
        print(" " + str(sets.R) + " " + str(sets.G) + " " + str(sets.B), end = ",")
    print()

given_set = SetsRGBValues(12, 13, 14)
id_impossible = []
for games in gamesList:
    for sets in games.sets:
       if sets.R > given_set.R:
           if games.id not in id_impossible:
               id_impossible.append(games.id)
       if sets.G > given_set.G:
           if games.id not in id_impossible:
               id_impossible.append(games.id)
       if sets.B > given_set.B:
           if games.id not in id_impossible:
               id_impossible.append(games.id)

id_possible = []
total_sum = 0
for games in gamesList:
    if games.id not in id_impossible:
        id_possible.append(games.id)
        total_sum += int(games.id)

print(id_possible)
print(total_sum)

total_cubes = 0
for max in gamesList:
    #print(max.maxRGBvalues)
    total_cubes += max.maxRGBvalues.R * max.maxRGBvalues.G * max.maxRGBvalues.B 
    print(str(max.maxRGBvalues.R) + " " + str(max.maxRGBvalues.G) + " " + str(max.maxRGBvalues.B))

print(total_cubes)
