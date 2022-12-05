from string import ascii_uppercase
def get_val(character, v):
    a = ascii_uppercase.index(character.capitalize())
    values[v] += a+27 if character.isupper() else a+1
def main(pri=True):
    global values
    values = [0,0,[]]
    for i, rucksack in enumerate(open("2022/DEC03/22DEC03.txt")):
        rucksack = rucksack.strip("\n")
        half = len(rucksack)//2
        ruck = set(rucksack[:half]).intersection(set(rucksack[half:]))
        intersector = ''.join(ruck)
        get_val(intersector, 0)
        if (i+1) % 3 == 0:
            ThirdVar = set(values[2][0]).intersection(set(values[2][1]), set(rucksack.strip("\n")))
            values[2].clear()
            get_val("".join(ThirdVar), 1)
        else:
            values[2].append(rucksack.strip('\n'))
    if pri: print(f"Total Value: {values[0]}\nTeam Value: {values[1]}")
if __name__ == '__main__':
    main()