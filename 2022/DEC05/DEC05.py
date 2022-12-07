matrix = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['T', ' ', 'Q', ' ', ' ', ' ', 'S', ' ', ' '],
    ['R', ' ', 'M', ' ', ' ', ' ', 'L', 'V', 'G'],
    ['D', 'V', 'V', ' ', ' ', ' ', 'Q', 'N', 'C'],
    ['H', 'T', 'S', 'C', ' ', ' ', 'V', 'D', 'Z'],
    ['Q', 'J', 'D', 'M', ' ', 'Z', 'C', 'M', 'F'],
    ['N', 'B', 'H', 'N', 'B', 'W', 'N', 'J', 'M'],
    ['P', 'G', 'R', 'Z', 'Z', 'C', 'Z', 'G', 'P'],
    ['B', 'W', 'N', 'P', 'D', 'V', 'G', 'L', 'T']
            ]

max_length = 0

crane_steps = open("DEC05.txt").readlines()[10:]
            
column_storage = []
column_destination = []
for instruction in crane_steps:
    instruction = instruction.strip("\n").split(" ")
    ins = [int(instruction[1]), int(instruction[3]), int(instruction[5])]

    for row in matrix: 
        if row[ins[1]-1] != " ":
            column_storage.append(row[ins[1]-1])
        if row[ins[2]-1] != " ":
            column_destination.append(row[ins[2]-1])

    for x in range(ins[0]):
        column_destination.reverse()
        column_destination.append(column_storage[0])
        column_destination.reverse()
        column_storage.pop(0)
    if len(column_destination) > max_length:
        max_length += len(column_destination) - max_length
    while len(column_storage) < len(matrix):
        column_storage.insert(0, " ")
    while len(column_destination) < len(matrix):
        column_destination.insert(0, " ")

    for i, row in enumerate(matrix):
        row[ins[1]-1] = column_storage[i]
        row[ins[2]-1] = column_destination[i]
    column_destination.clear()
    column_storage.clear()
for row in matrix: 
    if row != [" "," "," "," "," "," "," "," "," "]:
        print(f"[{row[0]}], [{row[1]}], [{row[2]}], [{row[3]}], [{row[4]}], [{row[5]}], [{row[6]}], [{row[7]}], [{row[8]}]")
print("---  ---  ---  ---  ---  ---  ---  ---  ---")