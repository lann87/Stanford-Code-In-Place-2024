import random

def main():
    dice = int(input("How many sides does your dice have? "))
# need to set (1, dice) because minimum value on most generic dice is 1)
    dice2 = str(random.randint(1, dice))
    print("Your roll is "+dice2)
if __name__ == '__main__':
    main()