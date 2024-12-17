# Each year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18  

def main():
    year = input("Enter an age in calendar years: ")
    year = int(year)
    year2 = input("That's " + str(year*7.18) + " in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()