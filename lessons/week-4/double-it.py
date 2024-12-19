def main():
    """
    You should write your code here. 
    """
    curr_value = int(input("Enter a number: "))
    while curr_value < 100:
        curr_value += curr_value
        print(curr_value)
    

if __name__ == '__main__':
    main()