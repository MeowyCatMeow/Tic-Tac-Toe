# for the while loop the better way is while " " in li hence while matrix doesn't have empty cells
li =[" " for x in range(9)]
threes = [li[:3], li[3:6], li[6:], li[0:9:3], li[1:9:3], li[2:9:3], li[0:9:4], li[2:7:2]]
def print_matrix():
    print("---------")
    print(f"| {li[0]} {li[1]} {li[2]} |")
    print(f"| {li[3]} {li[4]} {li[5]} |")
    print(f"| {li[6]} {li[7]} {li[8]} |")
    print("---------")

def win_check():
    if abs(li.count('X') - li.count('O')) >= 2 or ("XXX" in threes and "OOO" in threes):
        print("Impossible")
        return "end"
    elif ['X', 'X', 'X'] in threes:
        print("X wins")
        return "X"
    elif ['O', 'O', 'O'] in threes:
        print("O wins")
        return "O"
    # elif li.count('_') > 0 or li.count(' ') > 0:
    #    print("Game not finished")
    elif li.count(" ") == 0 and "XXX" not in threes and "OOO" not in threes:
        print("Draw")
        return "end"

def move():
    counter = 0
    global li, threes       
    while True:       
        move = input("Enter the coordinates:").split()    
        if (move[0].isnumeric() and move[1].isnumeric()) is False:
            print("You should enter numbers!")
            continue
        elif all(1 <= x <= 3 for x in (int(move[0]), int(move[1]))) is False:
            print("Coordinates should be from 1 to 3!")
            continue
        move = [int(x) for x in move]
        digit = (3 - move[0]) * 3 + (move[1] - 1)                           
        if li[digit] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            digit = (3 - move[0]) * 3 + (move[1] - 1) 
            if counter % 2 == 0:
                li[digit] = "X"
            else:
                li[digit] = "O"
            print_matrix()
            threes = [li[:3], li[3:6], li[6:], li[0:9:3], li[1:9:3], li[2:9:3], li[0:9:4], li[2:7:2]]
            state = win_check()
            if state == "X":           
                break
            elif state == "O":            
                break   
            elif state == "end":
                break
            counter += 1
            # print(threes)
print_matrix()
move()  
