def main(pri=True):
    Points, Points_2   = 0, 0
    #A = Rock, B = Paper, C = Scissors
    #X = Rock, Y = Paper, Z = Scissors
    Plays = {"X": [{"C": 6, "A": 3, "B": 0}, 1, 0], "Y": [{"A": 6, "B": 3, "C": 0}, 2, 3], "Z": [{"B": 6, "C": 3, "A": 0}, 3, 6]}
    Co_Plays = {"A": {"Z": 2, "Y": 1, "X": 3}, "B": {"Z": 3, "Y": 2, "X": 1}, "C": {"Z": 1, "Y": 3, "X": 2}}
    with open("2022/DEC02/22DEC02.txt") as games:
        for line in games:
            O, P = line.strip("\n").split(" ")
            Points   += Plays[P][0][O] + Plays[P][1]
            Points_2 += Co_Plays[O][P] + Plays[P][2]
    if pri: print(f"Points: {Points}\nPoints_2: {Points_2}")
if __name__ == '__main__':
    main()