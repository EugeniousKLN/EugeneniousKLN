# Full Name: Yauheni Kalionau, Jackson Morphew
# UCID: 30062335, 30068776


# Function handleInput takes user input as a parameter, and then checks
# if the user's input has "." (dot) at the end.Variable "extension" finds 
# "."(dot) in the user's input and returns an index: if extension is -1, 
# that means that there is no "."(dot) in the user input, so that the function 
# adds ".in" extension to the end. If extension is not -1(i.e. any other number),
# that means that there must be "."(dot) in the user's input and function has to 
# check whether or not it is ".in"(i.e. not .py,.jpeg,etc)
def handleInput(userInput):
    extension = userInput.find('.')
    if userInput.endswith('.in'):
        choosen_file = userInput
    elif extension == -1:
        choosen_file = str(userInput)+".in"
    return choosen_file


# Function openFile simply opens a file specified by user(userInput as a parameter) 
# and returns "already opened" inputFile which could be used in other functions. 
def openFile(userInput):
    inputFile = (open(handleInput(userInput),'r')).read()
    return inputFile        


# Function num_of_paragraphs takes userInput as a parameter and then creates a list 
# of paragraphs, where each element is separated from the previous one by an
# "empty line"(empty line=>'\n\n'). Finally, the function finds the length of this
# list, which is number of paragraphs in the text file.
def num_of_paragraphs(userInput):
    num_of_paragraphs = len(openFile(userInput).split('\n\n'))
    return num_of_paragraphs


# Function num_of_sentences_in_paragraphs again takes userInput as a parameter and 
# then loops through the list of paragraphs counting number of sentences for each 
# paragraph. It returns list of # of sentences with index corresponding to the index
# of pargraphs list.(i.e. index of num_of_sentences = index of list_of_paragraphs)
def num_of_sentences_in_paragraphs(userInput):
    list_of_paragraphs = openFile(userInput).split('\n\n')
    num_of_sentences = []
    punctuation_marks = ['.','!','?']
    for i in range(0,len(list_of_paragraphs)):
        paragraph = list_of_paragraphs[i]
        num_of_sentences_in_eachPar = []
        for punctuation_mark in punctuation_marks:
            num_of_sentences_in_eachPar.append(paragraph.count(punctuation_mark))
        num_of_sentences.append(sum(num_of_sentences_in_eachPar))
    return num_of_sentences


# Function num_of_words_in_paragraphs again takes userInput as a parameter and
# then "creates" a list of paragraphs by splitting input file on a newline.
# Then the function loops through every element in the "list_of_paragraphs"
# and counts number of words in each one(i.e. the function loops through
#  every paragraph). As a result, the function appends number of words in each
# paragraph to a new list and returns it. Every element in "words_in_paragraphs"
# has the same index as every element in "list_of_paragraphs" so that the values
# can be easily extracted for later use.
def num_of_words_in_paragraphs(userInput):
    list_of_paragraphs = openFile(userInput).split('\n\n')
    words_in_paragraphs = []
    for i in range(0,len(list_of_paragraphs)):
        paragraph = list_of_paragraphs[i]
        words_in_paragraphs.append(len(paragraph.split()))
        i = i + 1
    return words_in_paragraphs


        
# Function totalWords takes userInput as a parameter, opens text file by calling
# openFile function and then simply evaluates the lenght of the list of words in
# the text file which was "created" by using split() function.
def totalWords(userInput):
    total_num_of_words = len(openFile(userInput).split())
    return total_num_of_words



def most_common_words(userInput):
    list_of_words = openFile(userInput).split()
    count_words ={}  
    for word in list_of_words:
        if word.endswith('!'):
            word = word[:-1]
            count_words.update({word: openFile(userInput).count(word)})
        elif word.endswith('.'):
            word = word[:-1]
            count_words.update({word: openFile(userInput).count(word)})
        elif word.endswith('?'):
            word = word[:-1]
            count_words.update({word: openFile(userInput).count(word)})
        elif word.endswith(','):
            word = word[:-1]
            count_words.update({word: openFile(userInput).count(word)})
        elif word.endswith(';'):
            word = word[:-1]
            count_words.update({word: openFile(userInput).count(word)})
        else:
            count_words.update({word: openFile(userInput).count(word)})

            
    largest_value = max(count_words.values())
    
        
    return largest_value

    
# Function createOutput_file takes userInput as a parameter
# and creates new file called "report.in"and writes all 
# information obtained from previous functions into it.
# i.e. number of words,sentences and paragraphs is written 
# into this file by looping through each paragraph.
def createOutput_file(userInput):
    outputFile = open("report.in" ,"w+")
    paragraphs = num_of_paragraphs(userInput)
    sentences = num_of_sentences_in_paragraphs(userInput)
    words_count = num_of_words_in_paragraphs(userInput)
    outputFile.write("-----Total # of words in "+ userInput+ " is: " + str(totalWords(userInput)) + " words ------")
    k = 0
    for i in range(1,paragraphs+1):
        outputFile.write("\nparagraph number: " + str(i))
        outputFile.write("\n\tThere are " + str(words_count[k]) + " words in paragraph number " + str(i))
        outputFile.write("\n\tThere are " + str(sentences[k]) + " sentences in paragraph number " + str(i))
        k = k + 1
    





# main() function asks user to choose file and then calls different functions
# in order to first obtain information from the input file and then to 
# write required information to a new output file.
def main():
    userInput = input("Please choose file in the directory of your program: ")
    createOutput_file(userInput)
    main()
main()
