import random

NUM_PAIRS = 3

def main():
    #generate 2 pair per NUM_PAIR index
    num = 0
    numlst = []
    
    for num in range(NUM_PAIRS):
        for rep in range(2): #Generate a pair
            numlst.append(num) #Addinginto numlst
        num += 1

    random.shuffle(numlst) #Randomize numlst

    #Generate dlst with 2 Asterix x NUM_PAIRS
    displaylst = ['*' for _ in range(NUM_PAIRS * 2)]

    while '*' in displaylst:
        clear_terminal() 
        print(displaylst)
        compare_prompt(displaylst, numlst)
    
    print("Congratulations! You won!")



def compare_prompt(displaylst, numlst):
    index1 = index_prompt(displaylst)
    index2 = index_prompt(displaylst)

    #Check if same number entered twice.
    if index1 == index2:
        print("You entered the same index twice.")
        index2 = index_prompt(displaylst)
    
    #With valid input this prints out value of index1/2 in numlst
    
    if numlst[index1] == numlst[index2]:
        displaylst[index1] = numlst[index1]
        displaylst[index2] = numlst[index2]

        blank = input("Match!")
    else:    
        print(f"Value at index {index1} is {numlst[index1]}")
        print(f"Value at index {index2} is {numlst[index2]}")
        print("No match. Try again.")
        blankk = input("Press Enter to continue...")

    
def index_prompt(displaylst):    
    while True:
        try:
            index = int(input("Enter an index: "))
            #Checks both input with 0 and len of list
            if index < 0 or index >= len(displaylst):
                print("Invalid index. Try again.")
            
            #Checks if number has already been revealed
            elif displaylst[index] != '*':
                print("This number has already been matched. Try again.")
            else:
                return(index)
        
        #Checks if user entered non integer
        except ValueError:
            print("Not a number. Try again.")



def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()