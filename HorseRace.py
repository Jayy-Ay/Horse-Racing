import random as rand
import time
import sys

# Preparing to start the race.
def readyUp(t1, t2, t3, t4, t5):
    tDisplay1 = lineDisplay(t1)
    tDisplay2 = lineDisplay(t2)
    tDisplay3 = lineDisplay(t3)
    tDisplay4 = lineDisplay(t4)
    tDisplay5 = lineDisplay(t5)
    print(f'{tDisplay1}\n{tDisplay2}\n{tDisplay3}\n{tDisplay4}\n{tDisplay5}'), time.sleep(3)
    print("\n3..."), time.sleep(1)
    print("\n2..."), time.sleep(1)
    print("\n1..."), time.sleep(1)
    print("\nSTART!!!"), time.sleep(1)
    return True

# Racetrack Making
def lineMake(i):
    arr = ['_']*66                          # Race track is 60 + 2 for emoji, label + 4 for waiting zone
    arr[len(arr)-1] = str(f': Horse {i}')
    arr[len(arr)-2] = "🐎"
    arr[3] = '░'
    return arr

# Display beautified Racetrack in terminal 
def lineDisplay(arr):
    x = str(arr)                            # Turn to string to be able to remove symbols
    x = x.replace("[","")
    x = x.replace("]","")
    x = x.replace("'","")
    x = x.replace(",","")
    return x

# Roll D3 dice. Used for Movement
def roll(track, d1=1/3, d2=1/3, d3=1/3):   # Sum of bias is 1
    randRoll = rand.random()               # in [0,1)
    sum = 0
    result = 1
    for i in (d1,d2,d3):
        sum += i
        if randRoll < sum:
            return horseMove(track, result)       # If dont want to call funtion, replace with 'return result
        result+=1

# Horse Mover
def horseMove(line,move):
    # Finds horse
    pos = 0
    for i in range(len(line)):
        if (line[i] == "🐎"): pos = i
    # Moves horse
    line[pos-move] = "🐎"
    line[pos] = "_"
    # Check if horse finished race
    if (pos-move)!=3: line[3] = '░' # Fixes Finish Line
    if (pos-move) < 3:
        print(lineDisplay(line))        # Displays in Terminal
        return "w"
    else :
        print(lineDisplay(line))
        return line

if __name__ == '__main__':
    # Initializing a bunch of tracks, shortform t
    t1 = lineMake(1)
    t2 = lineMake(2)
    t3 = lineMake(3)
    t4 = lineMake(4)
    t5 = lineMake(5)

    bet = int(input("Which Horse will win; 1, 2, 3, 4 or 5? "))
    active = readyUp(t1, t2, t3, t4, t5)

    while (active):
        time.sleep(0.3)
        move1 = roll(t1); time.sleep(.005)
        move2 = roll(t2); time.sleep(.005)
        move3 = roll(t3); time.sleep(.005)
        move4 = roll(t4); time.sleep(.005)
        move5 = roll(t5); time.sleep(.005)
        #Checks for winner
        if (move1=="w"): winner = 1; break
        elif (move2=="w"): winner = 2; break
        elif (move3=="w"): winner = 3; break
        elif (move4=="w"): winner = 4; break
        elif (move5=="w"): winner = 5; break
        sys.stdout.write("\033[5A") # Move cursor up 5 steps in terminal
        sys.stdout.write("\033[J")  # Remove all lines till bottom (Make sure to be in this window for it to work)

    # Checking for Winner and Bet
    print(f"The Winning Horse is Horse {winner}!!!")
    if winner == bet: print("Your Horse won!")
    else : print("Your Horse didn't win :(")
    
