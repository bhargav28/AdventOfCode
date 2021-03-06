def calculateRow(string):
    low ,high = 0, 127
    for letter in string:
        if letter=="F":
            high = low + ((high- low)//2 )
        else :
            low =  high - ((high- low )//2 ) 
    return  low
def calculateCol(string):
    low ,high = 0, 7
    for letter in string:
        if letter=="L":
            high = low + ((high- low)//2 )
        else :
            low =  high - ((high- low )//2 ) 
    return  low
        
if __name__ == "__main__":
    with open('./Day5/input.txt') as f:
        id_list =  []
        for line in f :
            row = calculateRow(line[0:7])
            col = calculateCol(line[7:10])
            id = row*8 + col
            id_list.append(id)
        id_list.sort()
        for num in range(min(id_list),max(id_list)+1):
            if num not in id_list:
                print(num)