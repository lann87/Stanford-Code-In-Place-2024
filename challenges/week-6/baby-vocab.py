def main():
    #loading words var from the file.
    words = load_words_from_file("words.txt")
    babywords = {}
    #Iterate over each word in list
    for word in words:
        #Check if word is already in dict
        if word in babywords:
            #Increment count of word in dict
            babywords[word] += 1
        else:
            #Add in new word to dict
            babywords[word] = 1

    #Print the histo for each word and it's count
    for word, count in babywords.items():
        print_histogram_bar(word, count)

def print_histogram_bar(word, count):

    print(f"{word : <8}: {'x' * count}")

def load_words_from_file(filepath):
    """
    Loads words from a file into a list and returns it.
    We assume the file to have one word per line.
    Returns a list of strings. You should not modify this
    function.
    """
    words = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                words.append(cleaned_line)
    
    return words


if __name__ == '__main__':
    main()

    """
    Prints one bar in the histogram.
    
    Uses formatted strings to do so. The 
        {word : <8}
    adds white space after a string to make
    the string take up 8 total characters of space.
    This makes all of our words on the left of the 
    histogram line up nicely. On the other end,
        {'x' * count}
    takes the 'x' string and duplicates it by 'count'
    number of times. So 'x' * 5 would be 'xxxxx'.
    
    Calling print_histogram_bar("mom", 7) would print:
        mom     : xxxxxxx
    """