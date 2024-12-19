def main():
    #Setting the stones to always start at 20
    global stones
    stones = 20
    #Player 1 and 2's counter for next part
    p1 = 1
    p2 = 0

    #Selecting and executing code via player counters
    while stones > 0:
        print("There are " + str(stones) + " stones left.")
        if p1 > p2:
            sub = input("Player 1 would you like to remove 1 or 2 stones? ")
            if sub == "1" or sub == "2":
                stones -= int(sub)
                print()
                p2 += 1
            else:
                sub = input("Please enter 1 or 2: ")
                stones -= int(sub)
                print()
                p2 += 1

        else:
            sub = input("Player 2 would you like to remove 1 or 2 stones? ")
            if sub == "1" or sub == "2":
                stones -= int(sub)
                print()
                p1 += 1
            else:
                sub = input("Please enter 1 or 2: ")
                stones -= int(sub)
                print()
                p1 += 1
    
    if p1 > p2:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
    #print("Game over")

if __name__ == '__main__':
    main()