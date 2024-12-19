import random

def main():
    print("Khansole Academy")
    pts = 0
    while pts != 3:
        add1 = random.randint(10, 99)
        add2 = random.randint(10, 99)
        ans = add1 + add2
        print("What is " + str(add1) + " + " + str(add2) + "?")
        q = input("Your answer: ")
        if int(q) == ans:
            print("Correct!")
            pts += 1
            print("You've gotten " + str(pts) + " correct in a row.\n")
        else:
            print("Incorrect.")
            pts = 0
            print("The expected answer is ", ans, "\n")
    print("Congratulations! You mastered addition.")
    
    
if __name__ == '__main__':
    main()