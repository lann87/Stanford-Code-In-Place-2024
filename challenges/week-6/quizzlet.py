def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    score = 0    
    for rquiz, ans in translations.items():
        user_ans = input("What is the Spanish translation for " + rquiz + "?")
        if user_ans == ans:
            print("That is correct!")
            score += 1
        else:
            print("That is incorrect, the Spanish translation for " + rquiz + " is " + ans + ".")        
        print()
    print("You got " + str(score) + "/8 words correct, come study again soon!")

if __name__ == '__main__':
    main()