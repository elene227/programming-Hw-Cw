def mine_location(field):
    for i in range (len(field)):
        for c in range(len(field[i])):
            if field[i][c] == 1:
                return [i, c]
        
        