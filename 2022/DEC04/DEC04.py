def main(pri=True):
    Subsets  = Supersets = Intersections = 0
    allpairs  = []
    with open("2022/DEC04/22DEC04.txt") as ranges:
        for pair in ranges:
            pair = pair.strip("\n")
            partner_1, partner_2 = pair.split(",")[0].split("-"), pair.split(",")[1].split("-")
            partner_1, partner_2 = set(range(int(partner_1[0]),int(partner_1[1])+1)), set(range(int(partner_2[0]),int(partner_2[1])+1))
            allpairs.extend([partner_1, partner_2])
            if partner_1.issubset(partner_2) or partner_2.issubset(partner_1): Subsets += 1
            elif partner_1.intersection(partner_2): Intersections += 1
    for i, s in enumerate(allpairs):
        tempvar = set()
        for x in range(i+1, len(allpairs)):
            tempvar = tempvar | allpairs[x]
        for x in range(0, i):
            tempvar = tempvar | allpairs[x]
        if s.issubset(tempvar): Supersets += 1
    if pri: print(f"Subsets: {Subsets}, Supersets: {Supersets}, Intersections: {Intersections+Subsets}.")
if __name__ == "__main__": main()