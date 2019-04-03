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

def num_of_words_in_paragraphs(userInput):
    list_of_paragraphs = openFile(userInput).split('\n\n')
    words_in_paragraphs = []
    for i in range(0,len(list_of_paragraphs)):
        paragraph = list_of_paragraphs[i]
        words_in_paragraphs.append(len(paragraph.split()))
        i = i + 1
    return words_in_paragraphs


        


def totalWords(userInput):
    total_num_of_words = len(openFile(userInput).split())
    return total_num_of_words



def most_common_words(userInput):
    list_of_words = openFile(userInput).split()
    count_words = {}
    for word in list_of_words:
        count_words.update({word: openFile(userInput).count(word)})
    for big in count_words.values():
        
        
    return count_words

    








def main():


    userInput = input("Please choose file in the directory of your program: ")
    # y = totalWords(userInput)
    # x = num_of_paragraphs(userInput)
    print(most_common_words(userInput))
    print(num_of_words_in_paragraphs(userInput))
    print(num_of_sentences_in_paragraphs(userInput))
    # print("number of paragraphs:", x)
    # print("Total number of words: ", y)

    
    
    


    
    

    
    
    

    main()
main()




# assignment4.py
